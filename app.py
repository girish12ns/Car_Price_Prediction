
from flask import Flask,render_template,request
from src.data_pipline.predict_pipeline import Custom_data,Predict_Pipe



app=Flask(__name__)


@app.route('/')
def Hell_world():
    return render_template('home.html')



@app.route('/predictdata',methods=['GET','POST'])
def predict_data():
    if request.method=='POST':
        data=  Custom_data(
            name=request.form.get('name'),
            year=request.form.get('year'),
            km_driven=float(request.form.get('km_driven')),
            fuel=request.form.get('fuel'),
            seller_type=request.form.get('seller_type'),
            transmission=request.form.get('transmission'),
            owner=request.form.get('owner'),
            mileage=float(request.form.get('mileage')),
            engine=float(request.form.get('engine')),
            max_power=float(request.form.get('max_power')),
            seats=request.form.get('seats'),
            torque_only=float(request.form.get('torque_only')))

        df=data.get_the_data_frame()
        print(df)
        
        new_data=Predict_Pipe()
        result=new_data.predict_data(df)
        return render_template('home.html',results=result)



        




if __name__=='__main__':
    app.run(host="0.0.0.0",port=80)

