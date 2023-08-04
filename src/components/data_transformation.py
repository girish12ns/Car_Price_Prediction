
import os
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from  sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np
from src.utilis import save_object
from src.exception import customException
from src.logger import logging
import sys


class Data_transformationConfig:
    path=os.path.join('Artifacts','preprocessor.pkl')

class Dat_transformation:
    def __init__(self):
        self.data_transformation_config=Data_transformationConfig


    def data_transformation_object(self):

        num_features=['year', 'km_driven', 'mileage', 'engine', 'max_power',
                     'seats', 'torque_only']
        
        cat_features=['fuel', 'seller_type', 'transmission', 'owner']


        num_pip=Pipeline(steps=[
            ('imputer',SimpleImputer(strategy='mean')),
            ('scaler',StandardScaler())
            ])
        cat_pip=Pipeline(steps=[
           ('imputer',SimpleImputer(strategy='most_frequent')),
           ('encoder',OneHotEncoder())
            ])
        
        preprocessor=ColumnTransformer([
            ('num_pip',num_pip,num_features),
            ('cat_pip',cat_pip,cat_features)
            ])
        
        return preprocessor
    
    def data_transformation_iniated(self,train_path,test_path):
        logging.info("data_transformation_object_initited")
        try:
            train_df=pd.read_csv(train_path)

            test_df=pd.read_csv(test_path)


            target_variable='selling_price'

            preprocessor_obj=self.data_transformation_object()


            input_feature_train_df=train_df.drop(target_variable,axis=1)
            target_train_df=train_df[target_variable]

        
            input_feature_test_df=test_df.drop(target_variable,axis=1)
            target_test_df=test_df[target_variable]
        
            train_array=preprocessor_obj.fit_transform(input_feature_train_df)

            test_array=preprocessor_obj.transform(input_feature_test_df)

            train_ar=np.c_[train_array,np.array(target_train_df)]
            test_ar=np.c_[test_array,np.array(target_test_df)]

            logging.info("save object started")

            save_object(file_path=self.data_transformation_config.path,obj=self.data_transformation_config)

        
            return(
            train_ar,test_ar)
        except Exception as e:
            raise customException(e,sys)