#Import Standard Libraries
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

#Reading training data
data=pd.read_csv("final-student.csv",sep=";")

#Preprocessing data
del data["school"]

prediction_data = sys.argv[1]

cat_cols=["sex","address","famsize","Pstatus","Mjob",
          "Fjob","reason","guardian",'schoolsup',
          'famsup', 'paid', 'activities','nursery',
          'higher', 'internet', 'romantic']

for col in cat_cols:
    lbl = LabelEncoder()
    lbl.fit(list(data[col].values))
    data[col] = lbl.transform(list(data[col].values))

X=data.iloc[:,:31]
y=data.iloc[:,31]

prediction_data= lbl.transform(prediction_data)

result={"scores":[],"average":[],"pie_charts":[]}

result["average"].append(np.mean(np.mean(data.iloc[:,29:])))

linridge=Ridge(alpha=120).fit(X,y)

result["scores"]=prediction_data[29:31]
result["scores"].append(linridge.predict(prediction_data))

for idx,i in enumerate(data.columns[29:]):
        a=len(data[(data[i]>=18)])
        b=len(data[(data[i]>15) & (data[i]<18)])
        c=len(data[(data[i]>9) & (data[i]<=15)])
        d=len(data[(data[i]>4 ) & (data[i]<=9)])
        e=len(data[(data[i]>=0) & (data[i]<=4)])
        y=np.array([a,b,c,d,e])
        porcent = 100.*y/y.sum()
        result["pie_charts"].append(porcent)

print result
