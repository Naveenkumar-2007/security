import os 
import pandas as pd
import sys
import numpy as np
from networksecurity.logging.logger import logging
from networksecurity.exception.customexception import NetworkSecurityException
from networksecurity.entity.config import TRAINING_PIPLINE,TRAINING_DATA_INGESTION_CONFIG,DATAVALIDATION_CONFIG,DATATRANSFORMATION_CONFIG
from networksecurity.entity.artifects import DATA_INGESTION_AR,DATA_VALIDATION_AR,DataTransformationArtifact
from networksecurity.constant import trainpipeline
from networksecurity.components.data_ingestion import complete_dataingestion
from networksecurity.components.data_validation import datavalidation
from networksecurity.components.data_transform import DATA_TRANSFORM
if __name__=='__main__':
    data_training=TRAINING_PIPLINE()
    data_Data_ingestion=TRAINING_DATA_INGESTION_CONFIG(data_training)
    data_ingestion_file=complete_dataingestion(data_Data_ingestion)
    complete_ingestion=data_ingestion_file.final_convert()
    print(complete_ingestion)
    data_validation=DATAVALIDATION_CONFIG(data_training)
    data_validation_file=datavalidation(complete_ingestion,data_validation)
    data_file_valid=data_validation_file.intiate_data_validation()
    print(data_file_valid)
    data_transform=DATATRANSFORMATION_CONFIG(data_training)
    data_connect_transform=DATA_TRANSFORM(data_file_valid,data_transform)
    data_transform_complete=data_connect_transform.initiate_Transform()
    print(data_transform_complete)







