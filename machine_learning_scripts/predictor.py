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

cat_cols=["sex","address","famsize","Pstatus","Mjob",
          "Fjob","reason","guardian",'schoolsup',
          'famsup', 'paid', 'activities','nursery',
          'higher', 'internet', 'romantic']

for col in cat_cols:
    lbl = LabelEncoder()
    lbl.fit(list(data[col].values))
    data[col] = lbl.transform(list(data[col].values))

#Assigning and train_test_split
X=data.iloc[:,:31]
y=data.iloc[:,31]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=1)

#Training the model
linridge=Ridge(alpha=120).fit(X_train,y_train)

print r2_score(y_test,linridge.predict(X_test))

#Integration with Django framework yet to be done
