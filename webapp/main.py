from flask import Flask,render_template,request
import joblib
import numpy as np
from keras.models import load_model
from keras import backend as K

model=load_model('models/model-167.keras')            #api hadapu best model eka damai

scaler_data=joblib.load('models/scaler_data.sav')
scaler_target=joblib.load('models/scaler_target.sav')

app=Flask(__name__) #application

def prediction(lst):
		lst=scaler_data.transform([lst])	 #scaling the features before applying to the model
		pred_value = model.predict(lst) 
		pred_value=scaler_target.inverse_transform(pred_value) #inverse scaling the prediction(target) before returning
		print(pred_value,pred_value[0],pred_value[0][0])  
		return pred_value
		

@app.route('/')
def index():

	return render_template('patient_details.html')

@app.route('/getresults',methods=['POST'])
def getresults(): 
	result=request.form 
	print(result)

	name=result['name']
	gender=result['gender']
	age=result['age']
	tc=result['tc']
	hdl=result['hdl']
	smoke=result['smoke']
	bpm=result['bpm']
	diab=result['diab']

	print("h1")
	feature_list = []  

	def gender_list(value):
		print("h1")
		if value == "Female":
			feature_list.append(0)
		elif value =="Male":
			feature_list.append(1)
	
	def yesno_list(value):
		if value == "Yes":
			feature_list.append(1)
		elif value == "No":
			feature_list.append(0)
	
	
	gender_list(gender)
	feature_list.append(int(age))
	feature_list.append(int(tc))
	feature_list.append(int(hdl))
	yesno_list(smoke)
	yesno_list(bpm)
	yesno_list(diab)
	
	pred_value = prediction(feature_list)
	resultDict={"name":name,"risk":round(pred_value[0][0],2)}

	return render_template('patient_results.html',results=resultDict)

app.run(debug=True)