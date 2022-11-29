from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
# def test_exception():
#     try:
#         logging.info("we are dividing be 0")
#         x=65656/0
#     except Exception as e:
#         raise SensorException(e,sys)

# if __name__ == '__main__':
#     Training_Pipeline_Config = TrainingPipelineConfig()
#     Data_Ingestion_Config = DataIngestionConfig(Training_Pipeline_Config)
#     print(Data_Ingestion_Config.__dict__)
    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)
    # mongodb_client = MongoDBClient()
    # print(mongodb_client.database.list_collection_names())

if __name__ == '__main__':
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()