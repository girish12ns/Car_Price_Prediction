from src.exception import customException
from src.logger import logging
import pandas as pd
from src.utilis import load_object
import sys
import os


class Predict_Pipe:
    def __init__(self):
        pass

    def predict_data(self,features):
        try:
            model_path=os.path.join('Artifacts','Model.pkl')
            preprocessor_path=os.path.join('Artifacts','preprocessor.pkl')

            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)

            scaled_data=preprocessor.transform(features)

            predict=model.predict(scaled_data)

            return predict
        except Exception as e:
            raise customException(e,sys)







class Custom_data:
    def __init__(self,name, year,km_driven,fuel,seller_type,
       transmission, owner, mileage, engine, max_power, seats,
       torque_only):
        self.name=name
        self.year=year
        self.km_driven=km_driven
        self.fuel=fuel
        self.seller_type=seller_type
        self.transmission=transmission
        self.owner=owner
        self.mileage=mileage
        self.engine=engine
        self.max_power=max_power
        self.seats=seats
        self.torque_only=torque_only

    def get_the_data_frame(self):
        
        custom_data={
            'name':[self.name],
            'year':[self.year],
            'km_driven':[self.km_driven],
            'fuel':[self.fuel],
            'seller_type':[self.seller_type],
            'transmission':[self.transmission],
            'owner':[self.owner],
            'mileage':[self.mileage],
            'engine':[self.engine],
            'max_power':[self.max_power],
            'seats':[self.seats],
            'torque_only':[self.torque_only]}
        
        custom_df=pd.DataFrame(custom_data)

        return custom_df


