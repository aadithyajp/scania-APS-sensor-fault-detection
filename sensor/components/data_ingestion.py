from sensor.exception import SensorException
from sensor.logger import logging
from sklearn.model_selection import train_test_split
import os,sys
from pandas import DataFrame
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.data_access.sensor_data import SensorData
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    
    def __init__(self,Data_Ingestion_Config:DataIngestionConfig):
        try:
            self.Data_Ingestion_Config=Data_Ingestion_Config
            
        except Exception as e:
            raise SensorException(e,sys)
    
    def export_data_into_feature_store(self) -> DataFrame:
        """
        export mongo db collection as data frame into feature
        """ 
        try:
            logging.info("exporting data from mongodb to feature store")
            Sensor_Data = SensorData()
            dataframe= Sensor_Data.export_collection_as_dataframe(collection_name=self.Data_Ingestion_Config.collection_name)
            feature_store_file_path = self.Data_Ingestion_Config.feature_store_file_path
            
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        
        except Exception as e:
            raise SensorException(e,sys)
            
    
    def split_data_as_train_test(self, dataframe:DataFrame) -> None:
        """
        feature store dataset will be split into train and test file 
        """
        
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.Data_Ingestion_Config.train_test_split_ratio)

            logging.info("Performed train test split on the dataframe")

            logging.info("Exited split_data_as_train_test method of Data_Ingestion class")

            dir_path = os.path.dirname(self.Data_Ingestion_Config.training_file_path)

            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Exporting train and test file path.")

            train_set.to_csv(self.Data_Ingestion_Config.training_file_path, index=False, header=True)

            test_set.to_csv(self.Data_Ingestion_Config.testing_file_path, index=False, header=True)

            logging.info(f"Exported train and test file path.")
            
        except Exception as e:
            raise SensorData(e,sys)
        
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            DataFrame = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe=DataFrame)
            Data_Ingestion_Artifact= DataIngestionArtifact(trained_file_path=self.Data_Ingestion_Config.training_file_path,
            test_file_path=self.Data_Ingestion_Config.testing_file_path)
            return Data_Ingestion_Artifact
        
        except Exception as e:
            raise SensorException(e,sys)