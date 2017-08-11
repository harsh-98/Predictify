#Import Standard Libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import sys
import os

def billu_scorer(data2):
    #Reading training data
    data=pd.read_csv("final-student.csv",sep=";")
    #Preprocessing data
    del data["school"]

    prediction_data = np.array(data2)
    # prediction_data = np.array([sys.argv[i] for i in range(1,32)])

    #sample data='F' 15 'U' 'GT3' 'T' 4 2 'health' 'services' 'home' 'mother' 1 3 0 'no' 'yes' 'yes' 'yes' 'yes' 'yes' 'yes' 'yes' 3 2 2 1 1 5 2 15 14
    #example python new.py 'F' 15 'U' 'GT3' 'T' 4 2 'health' 'services' 'home' 'mother' 1 3 0 'no' 'yes' 'yes' 'yes' 'yes' 'yes' 'yes' 'yes' 3 2 2 1 1 5 2 15 14

    prediction_data.shape=(1,31)

    final_prediction=pd.DataFrame(prediction_data,columns=np.array(data.columns[:31]))

    cat_cols=["sex","address","famsize","Pstatus","Mjob",
              "Fjob","reason","guardian",'schoolsup',
              'famsup', 'paid', 'activities','nursery',
              'higher', 'internet', 'romantic']

    for col in cat_cols:
        lbl = LabelEncoder()
        lbl.fit(list(data[col].values))
        data[col] = lbl.transform(list(data[col].values))
        final_prediction[col]=lbl.transform(list(final_prediction[col].values))

    X=data.iloc[:,:31]
    y=data.iloc[:,31]


    result={"scores":[],"average":[],"pie_charts":[]}

    result["average"].append(np.mean(np.mean(data.iloc[:,29:])))

    linridge=Ridge(alpha=120).fit(X,y)

    result["scores"]=final_prediction.values[0,29:31].tolist()
    result["scores"]=[float(i) for i in result["scores"]]

    result["scores"].append((linridge.predict(final_prediction)[0]))

    for idx,i in enumerate(data.columns[29:]):
            a=len(data[(data[i]>=18)])
            b=len(data[(data[i]>15) & (data[i]<18)])
            c=len(data[(data[i]>9) & (data[i]<=15)])
            d=len(data[(data[i]>4 ) & (data[i]<=9)])
            e=len(data[(data[i]>=0) & (data[i]<=4)])
            y=np.array([a,b,c,d,e])
            porcent = 100.*y/y.sum()
            result["pie_charts"].append(porcent.tolist())

    return result
