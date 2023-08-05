import os
from src.exception import customException
import sys
import dill

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from math import *
from sklearn.model_selection import GridSearchCV

try:
    def save_object(file_path,obj):
        
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,"wb") as file_object:
            dill.dump(obj,file_object)
except Exception as e:
    raise customException(e,sys)

try:
    def model_evaluation(true,prediction):
        #mse=mean_squared_error(true,prediction)
        #mae=mean_absolute_error(true,prediction)
        #rmse=sqrt(mse)
        score=r2_score(true,prediction)
        return score

    def model(x_train,x_test,y_train,y_test,models:dict):
        model_list=[]
        r2_score_list=[]
        for i in range(len(list(models))):
            model=list(models.values())[i]
    
            #fitting the model
            model.fit(x_train,y_train)
    
            #prediction
            model_predict=model.predict(x_test)
    
            score=model_evaluation(y_test,model_predict)
    
            model_list.append(list(models.keys())[i])
    
            r2_score_list.append(score)
            
        return model_list,r2_score_list
    
except Exception as e:
    raise customException(e,sys)

try:
    def load_object(file_path):

        with open(file_path,"rb") as file_object:
            return dill.load(file_object)
except Exception as e:
    raise customException(e,sys)