import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
data=pd.read_csv("/home/harsh/Desktop/Andha-Predictor/machine_learning_scripts/final-student.csv",sep=";")
del data["school"]
np.unique(data["address"])
cat_cols=["sex","address","famsize","Pstatus","Mjob","Fjob","reason","guardian",'schoolsup', 'famsup', 'paid', 'activities','nursery', 'higher', 'internet', 'romantic']

for col in cat_cols:
    lbl = LabelEncoder()
    lbl.fit(list(data[col].values))
    data[col] = lbl.transform(list(data[col].values))
X=data.iloc[:,:31]
y=data.iloc[:,31]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=1)
linridge=Ridge(alpha=120).fit(X,y)
def graph_():
 return [(1,2,3), data.iloc[2,29],data.iloc[2,30],data.iloc[2,31], np.mean(np.mean(data.iloc[:,29:]))]
def pie_():
    arr_=list()
    arr_.append(["A","B","C","D","E"])
    for idx,i in enumerate(data.columns[29:]):
        a=len(data[(data[i]>=18)])
        b=len(data[(data[i]>15) & (data[i]<18)])
        c=len(data[(data[i]>9) & (data[i]<=15)])
        d=len(data[(data[i]>4 ) & (data[i]<=9)])
        e=len(data[(data[i]>=0) & (data[i]<=4)])
        arr_.append([a,b,c,d,e])
    return arr_