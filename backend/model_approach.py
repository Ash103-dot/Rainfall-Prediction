# -*- coding: utf-8 -*-
"""model_approach.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gOB1bwqTyC6mm6KgPvJceFfxswd61Hmz

# Instructions
You can use this notebook for **Task 1**

You can import the libraries that you need.
For instance:
```python
from sklearn.metrics import mean_squared_error
```

Please load the datasets that will be provided:
- Right-click and select upload from the left panel
- Select the files (*Japan_cities_rainfall.csv*, *rainfall_to_predict.csv*)


Below is the function to verify your final predictions based on the *rainfall_to_predict.csv* file.

**Please run it before starting**

#### Function to verify your prediction score
##### Root Mean Square Error

In order to verify the accuracy of you model, use the _verify_predictions_ function with your predictions results
```python
verify_predictions(output_result)

# returns {"result":RMSE_RESULT_VALUE,"type":"rmse"}
```
"""

# Please do not modify
import requests
import json

def verify_predictions(y_pred):
    
    url = "https://q7wmplg8u6.execute-api.ap-northeast-1.amazonaws.com/dev"
    
    payload = {
        "submission": y_pred
    }
    response = requests.request("POST", url,data=json.dumps(payload),headers = {'content-type': 'application/json'})
    
    return response.text

"""#Start your task from below

# Code for the Rainfall prediction

---
"""

# imports
import numpy as np
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

from google.colab import drive
drive.mount('/content/drive')

# loading the datasets
df = pd.read_csv('/content/drive/MyDrive/wni/Japan_cities_rainfall.csv')
df_to_predict = pd.read_csv('/content/drive/MyDrive/wni/rainfall_to_predict.csv')

df.head()

df_to_predict.head()

def breakdown_month(a):
  if(a[4:6]=='9'):
      return 0
  elif(a[4:6]=='10'):
      return 1
  else:
      return 2
def breakdown_date(a):
  return int(a[6:8])
def breakdown_time(a):
  if(int(a[9:11])>=0 and int(a[9:11])<6):
    return 1
  elif(int(a[9:11])>=6 and int(a[9:11])<12):
    return 2
  elif(int(a[9:11])>=12 and int(a[9:11])<18):
    return 3
  elif(int(a[9:11])>=18 and int(a[9:11])<24):
    return 4

city_mapping = {" Naha": 1, " Fukuoka": 2, " Sendai": 3, " Osaka": 4, " Nigata": 5, " Tokyo": 6}
datasets=[df,df_to_predict]
cols=['date','month','time','city','rainfall']
for data in datasets:
  data['city']=data['place'].map(city_mapping)
  data['month']=data['date_time'].apply(breakdown_month)
  data['date']=data['date_time'].apply(breakdown_date)
  data['time']=data['date_time'].apply(breakdown_time)
  data.drop(['place','longitude','latitude','date_time'],axis=1,inplace=True)
df=df[cols]
df_to_predict=df_to_predict[cols[:-1]]

df.head()

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor  
Y=df['rainfall']
X=df.drop('rainfall',axis=1)
gbr_model=GradientBoostingRegressor()
gbr_model.fit(X, np.ravel(Y))
pred=gbr_model.predict(df_to_predict)
pred=pred.tolist()
result_rmse = verify_predictions(pred)
print(result_rmse)
print(df_to_predict[:10])
print(pred[:10])

from flask import Flask,jsonify
import requests, json
import pickle

data=[
{'date':'2020-02-19','place':'naha','time':'060000','pred':0.22822961314619528},
{'date':'2020-02-19','place':'naha','time':'170000','pred':0.139062199458239},
{'date':'2020-02-19','place':'naha','time':'200000','pred':0.13361914782113052},
{'date':'2020-11-19','place':'sendai','time':'183000','pred':0.02135037157824171},
{'date':'2020-11-19','place':'nigata','time':'230000','pred':0.10497764087733633}]

app=Flask(__name__)
if __name__=="__main__":
    app.run(debug=True)

@app.route('/data',methods=['GET'])
def get():
    return jsonify({"Data":data})

pickle.dump(gbr_model,open('gbr_model.pkl','wb'))

my_gbr=pickle.load(open('gbr_model.pkl','rb'))

my_gbr

url="http://127.0.0.1:5000/"
data=json.dumps({'date':19,'month':0,'time':1,'city':1})
r=requests.post(url,data)
print(r.json())