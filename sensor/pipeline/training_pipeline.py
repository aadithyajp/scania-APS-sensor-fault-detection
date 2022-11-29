from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.exception import SensorException
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.components.data_ingestion import DataIngestion
import sys,os
from sensor.logger import logging

class TrainPipeline:
    
    def __init__(self):
        Training_Pipeline_Config = TrainingPipelineConfig()
        self.Data_Ingestion_Config = DataIngestionConfig(Training_Pipeline_Config)
        self.Training_Pipeline_Config = Training_Pipeline_Config
        
        
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
        
    def start_data_validation(self):
        try:
            pass
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
            Data_Ingestion_Artifact:DataIngestionArtifact=self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e,sys)