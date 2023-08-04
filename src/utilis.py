import os
from src.exception import customException
import sys
import dill

try:
    def save_object(file_path,obj):
        
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,"wb") as file_object:
            dill.dump(file_object,obj)
except Exception as e:
    raise customException(e,sys)
