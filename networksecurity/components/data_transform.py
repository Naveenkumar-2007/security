
import os 
import pandas as pd
import sys
import numpy as np
from networksecurity.logging.logger import logging
from networksecurity.exception.customexception import NetworkSecurityException
from networksecurity.constant import trainpipeline
from networksecurity.constant.trainpipeline import shema,TARGET_COLUMN,DATA_IMPUTER_PARAMS
from networksecurity.entity.config import DATATRANSFORMATION_CONFIG
from networksecurity.entity.artifects import DATA_VALIDATION_AR,DataTransformationArtifact
from networksecurity.utilsfile.util import read_shema,write_yaml_file,save_numpy_array_data,save_object
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
class DATA_TRANSFORM:
    def __init__(self,data_validation:DATA_VALIDATION_AR,
                 data_transform_config:DATATRANSFORMATION_CONFIG):
        
        try:
            self.data_validation:DATA_VALIDATION_AR=data_validation
            self.data_transform_config:DATATRANSFORMATION_CONFIG=data_transform_config
        except Exception as ex:
            raise NetworkSecurityException(ex,sys)
        
    @staticmethod
    def read_shema(filepath)->pd.DataFrame:
        try:
            return pd.read_csv(filepath)
        except Exception as ex:
            raise NetworkSecurityException(ex,sys)
        
    def get_perprocessing(cls)->Pipeline:
        try:
            imputer:KNNImputer=KNNImputer(**DATA_IMPUTER_PARAMS)
            perproce:Pipeline=Pipeline([('imputer',imputer)])
            return perproce

        except Exception as ex:
            raise NetworkSecurityException(ex,sys)
        

        

        
    def initiate_Transform(self)->DataTransformationArtifact:
        try:
            trainingdata=self.data_validation.data_valid_train
            testingdata=self.data_validation.data_valid_test
            train_df=DATA_TRANSFORM.read_shema(trainingdata)
            test_df=DATA_TRANSFORM.read_shema(testingdata)
            #training data
            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1, 0)

            #testing dataframe
            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1, 0)

            preprocessor=self.get_perprocessing()

            preprocessor_object=preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature=preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature =preprocessor_object.transform(input_feature_test_df)
             

            train_arr = np.c_[transformed_input_train_feature, np.array(target_feature_train_df) ]
            test_arr = np.c_[ transformed_input_test_feature, np.array(target_feature_test_df) ]

            #save numpy array data
            save_numpy_array_data( self.data_transform_config.transformed_train_file_path, array=train_arr, )
            save_numpy_array_data( self.data_transform_config.transformed_test_file_path,array=test_arr,)
            save_object( self.data_transform_config.transformed_object_file_path, preprocessor_object,)

            #save_object( "final_model/preprocessor.pkl", preprocessor_object,)



        except Exception as ex:
            raise NetworkSecurityException(ex,sys)

