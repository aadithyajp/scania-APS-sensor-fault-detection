from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.exception import SensorException
from sensor.entity.artifact_entity import DataIngestionArtifact
import sys,os
from sensor.logger import logging

class TrainPipeline:
    
    def __init__(self):
        Training_Pipeline_Config = TrainingPipelineConfig()
        self.Data_Ingestion_Config = DataIngestionConfig(Training_Pipeline_Config)
        self.Training_Pipeline_Config = Training_Pipeline_Config
        
        
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("starting data ingestion")
            logging.info("data ingestion completed")
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