

from src.exception import customException
from sklearn.model_selection import train_test_split
from src.logger import logging
import os
import pandas as pd
import sys
from src.components.data_transformation import Dat_transformation
from src.components.model_trainer import Model_Trainer
from dataclasses import dataclass

@dataclass
class DataingestionConfig:
    train_path=os.path.join("Artifacts",'train.csv')
    test_path=os.path.join('Artifacts','test.csv')
    raw_data_path=os.path.join('Artifacts','raw.csv')

class Data_ingestion:
    def __init__(self):
        self.data_ingestion_config=DataingestionConfig


    def data_ingestion_intiated(self):
        try:
            car_df=pd.read_csv('NOTE BOOK\data\Cleaned_dataset.csv')


            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)

            car_df.to_csv(self.data_ingestion_config.raw_data_path,header=True,index=False)

            train_set,test_set=train_test_split(car_df,test_size=0.2,random_state=42)

            train_set.to_csv(self.data_ingestion_config.train_path,header=True,index=False)

            test_set.to_csv(self.data_ingestion_config.test_path,header=True,index=False)


            return(self.data_ingestion_config.train_path,self.data_ingestion_config.test_path)
        except Exception as e:
            raise customException(e,sys)
        
if __name__=="__main__":

    data=Data_ingestion()
    train_set,test_set=data.data_ingestion_intiated()

    transfomation=Dat_transformation()
    x_train,x_test,y_train,y_test=transfomation.data_transformation_iniated(train_set,train_set)

    Trainer=Model_Trainer()
    Trainer.Model_trainer_object(x_train,x_test,y_train,y_test)
