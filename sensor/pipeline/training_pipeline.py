from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation 

# from sensor.components
from sensor.data_access.sensor_data import SensorData
from sensor.logger import logging
from sensor.exception import SensorException
import sys,os
class TrainPipeline:
    
    def __init__(self):
       self.Training_Pipeline_Config = TrainingPipelineConfig()
        # self.Data_Ingestion_Config = DataIngestionConfig(Training_Pipeline_Config)
        # self.Training_Pipeline_Config = Training_Pipeline_Config
        
        
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            self.Data_Ingestion_Config = DataIngestionConfig(training_pipeline_config=self.Training_Pipeline_Config)
            logging.info("starting data ingestion")
            data_ingestion = DataIngestion(Data_Ingestion_Config=self.Data_Ingestion_Config)
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"data ingestion completed and artifact:{data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.Training_Pipeline_Config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config = data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
        
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
    
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            
        except Exception as e:
            raise SensorException(e,sys)