# sensor-fault-detection
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.


### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.
## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions


## This is the architecture of IOT sensor ML project

1. create  a virtual environment with python
3. add readme.md file ,git ignore file and requirements.txt file
4. next step is most important...SETUP.PY file :
	1. this setup script is the centre of all activity in building, distributing, and installing modules The main purpose of the setup script is to describe your module distribution to the Distutils, so that the various commands that operate on your modules do the right thing
5. sensor folder is the master folder and we creating our own package everything will be inside this sensor folder 
		1. pipeline: we can have training pipeline for prediction as well as for training 
		2. ML: any custom model, accuracy, graph,or feature engineering related code goes under ML folder (for training the model we write code inside the ml\model folder) and we write evaluation metrics code inside ml\metric
		3. entity: entity folder to define structure for input and output of every ML component. in ML components we have multiple components in pipeline so we have to define what is the input and output of each component 
		4. data_access: if our data is in mongo db database we have to extract from it soo we write those codes here
		5. constant: is something that won't change like file name model name or database name but we have to decide initially 
		6. configuration: to maintain all project related connection configuration and connection related code we will be writing it in configuration folder
		7. components: Machine learning pipelines consist of multiple sequential steps that do everything from data extraction and preprocessing to model training we will be writing ML components here 
		9. cloud_storage: is about how we can manage file across cloud for like upload or download a file we can write code and it will done automatically 
		10. logger: this is part of every project what is happening inside your code it should be logged 
		11. exception: this is part of every project if abnormality is happening we have to capture it properly so that we can modify our code that the same error will not happen again with logger and exception we can audit the code to figure out the process of the project works
		12. util: when ever we require a common code in multiple places we write a function inside it and use to call wherever we want
		13. estimator:in this file we will assign the custom mapping function for target variable 


### High Level Code Flow For Sensor Fault Detection
![0_Sensor Training Pipeline](https://user-images.githubusercontent.com/97959379/207000736-a7123f19-2cb7-47c6-8d7f-aa8473f23a20.png)



every component building starts from :   constant(training pipeline)  ->  entity (config/artifact) -> components


### data ingestion:



![1_Sensor_Data Ingestion Component](https://user-images.githubusercontent.com/97959379/207002886-2683e6f5-afc2-4355-b3e8-e4a1802bac6e.png)



step 1:


1. we will decide values for these variables (( data ingestion dir,  feature store file path,  training file path,  testing file path,  train test split ratio,  collection name)) for our data ingestion config (IN CONFIG_ENTITY)

step 2:

1. and then we initiate data ingestion operations were first of all we extract data from mongo db and we created a sensor.csv file 

step3:

1. export data to feature store starts were it has 2 operations to do 

step 3.1:

1. extract data from mongo db database and stored it in feature store folder via (( data ingestion artifact /with time stamp/feature store/as a .csv file)) 

step4:

1. and the unwanted columns are dropped using the script we wrote in schema file which is located in config folder

step5:

1. from sensor.csv we splitted it into train.csv and test.csv  with the split ratio of 0.2  and stored it into data ingested folder via (( feature store/with time stamp/as a train and test split))




### data validation:




![2_Sensor_Data Validation Component ](https://user-images.githubusercontent.com/97959379/207002926-a42417f1-90ce-45a0-aa2e-7bc2d80eabd2.png)




step1:

1. we will decide values for these variables ((data validation dir,  valid data dir,  invalid data dir,  valid train file path, invalid train file path, invalid test file path, drift report file path)) for our data validation config (IN CONFIG_ENTITY)

step2:

1. and then we initiate data validation operations and we obtain data from data ingestion artifact / from data ingested folder 
2. we obtain train and test csv file from data ingested folder and to read data

step3:

1. in validate number of columns we will check all columns are present in train and test csv file if columns are missing in training or test file the result will pass on to validation status and raise validation error

step4:

1. in (is numerical column exist) we will check all numerical columns are present in train and test csv file if columns are missing in training or test file the result will pass on to validation status and raise validation error

step5:

1. in validation status if any of columns is missing in train or test it will raise validation  error or if its all True we will go for the data drift

step6:

1. in detect dataset drift we will check the data drift status and then we pass on to data validation  artifact and the report.yaml file with timestamp will be saved




### data transformation:




![3_Sensor_Data_Transformation_Component](https://user-images.githubusercontent.com/97959379/207002953-6f8d934f-40bd-4699-9714-fb04bf85c6d2.png)


step1:

1. we will set the data transformation config with essential files and then we initiate data transformation
2. we obtain train and test file from data validation artifact and then we read data 

step2:

1. TRAIN DATAFRAME: we are getting the train data set and gonna start process it
   

step2a, step3a:

1. we are segregating input feature and target feature
   
2. for the INPUT FEATURE we gonna apply data transformation
3. for TARGET FEATURE  we are mapping its categorical value like (0=positive, 1=negative)

step4:

1. robust scaler is used to detect and take care of outliers and scale down every feature to similar scale and simpler imputer to take care of missing values
2. after that  we get a preprocessing object using this we gonna transform our train and test dataset


step5:

1. using SMOTETOMEK we will handle the imbalance  dataset and balance our classes

step6:

1. after that we will join our input feature and target feature of train and test dataset and save it as train.numpy array and test .numpy array into data transformation artifact folder


### data model training:


![4_Sensor_Model Trainer Component](https://user-images.githubusercontent.com/97959379/207003007-7373d6c7-3776-4e29-a1b4-b6d018e4d8d2.png)





step1:

1. we have to set the model trainer config with essential file paths, in this component the model will trained using the best ml model which gave the best score in EDA part 
2. after the model trainer config we initiate model trainer and we obtain train and test np array data from data transformation artifact for that we will use load numpy array  data after that train will be split as x_train and y_train , test will be split as y_train and y_test

step2:

1. after we fit  the model to train data with best algorithm we check for metrics score if the metrics score of train data is <= to the expected accuracy we will raise a exception if passed 
2. then we fit with test data and check for metrics score after that we check for over fitting and under fitting and difference should be > the value we set

step3:

	1. after we get the best model we have to save the (best model and preprocessed obj) in file name sensor model



### data evaluation:




![5_Sensor Model Evaluation Component](https://user-images.githubusercontent.com/97959379/207003051-59b59d6f-b53f-4e7a-874f-d64fcaaff35d.png)


step1:

1. model evaluation config must be setup with essential files mentioned and initiating model evaluation and we obtain input from data validation artifact and model trainer artifact
2. we obtain valid train and test file path from data validation artifact and concat them assign them the target mapping

step2:

1. and then we obtain the previously stored sensor model and we evaluate the current model with the sensor model
2. we will then check the metric score of current model if the metrics is higher and improved then we push that to model evaluation artifact



### sensor model pusher:




![6_Sensor Model Pusher Component](https://user-images.githubusercontent.com/97959379/207003075-b8769e20-4c92-4633-8203-085ace2a5a0e.png)



step1:

1. we have to setup model pusher config file and after initiation of model pusher the objective is it will create a folder saved model inside the model is saved and we get a model pusher artifact
2. after that we have to set env variable for AWS secret keys and we will push our all artifacts folder to s3 bucket and we also push our saved model to s3 bucket 
3. next we can run all this in AWS EC2 for that we can dockerise it and with the help of CI/CD pipleline from github actions we can do this operations




### Step 1: Clone the repository
```bash
git clone https://github.com/sethusaim/Sensor-Fault-Detection.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n sensor python=3.7.6 -y
```

```bash
conda activate sensor
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="your own db"

```






