import os
import sys
from src.exception import customException
from src.logger import logging
import pandas as pd
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from src.utilis import model,save_object


from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from dataclasses import dataclass






@dataclass
class Model_trainerConfig:
    model=os.path.join('Artifacts','Model.pkl')

class Model_Trainer:
    def __init__(self):
        self.model_trainer_config=Model_trainerConfig()

    def Model_trainer_object(self,x_train,x_test,y_train,y_test):
        try:
            models={'LinearRegression':LinearRegression(),
            'Lasso':Lasso(alpha=0.1,max_iter=10000),
            'Ridge':Ridge(),
            'KNeighborsRegressor':KNeighborsRegressor(),
            'SVR':SVR(),
            'DecisionTreeRegressor':DecisionTreeRegressor(),
            'RandomForestRegressor':RandomForestRegressor(),
            'GradientBoostingRegressor':GradientBoostingRegressor(),
            'CatBoostRegressor':CatBoostRegressor(),
            'XGBRegressor':XGBRegressor()}
        
        

            r2_score_list,model_list=model(x_train=x_train,x_test=x_test,y_train=y_train,
                                       y_test=y_test,models=models)
        
            best_model={}
            for mode,score in zip(model_list,r2_score_list):
                best_model[mode]=score

            best_model=sorted(best_model.items(),key=lambda x:x[1],reverse=True)

            Highest_score_model=models[best_model[0][1]]

            print(best_model)

            print(Highest_score_model)
            Highest_score_model.fit(x_train,y_train)

            predict=Highest_score_model.predict(x_test)

            r2_score_best=r2_score(y_test,predict)

            print(r2_score_best)

            save_object(file_path=self.model_trainer_config.model,obj=Highest_score_model)

        except Exception as e:
            raise Exception(e,sys)
        
        save_object(file_path=self.model_trainer_config.model,obj=Highest_score_model)







        


    



        