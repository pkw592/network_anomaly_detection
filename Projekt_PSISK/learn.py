import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
import matplotlib.pyplot as plt

data = pd.read_csv('data_i2.txt', sep=';',low_memory=False)

data = data[['ip1_1','ip1_2','ip1_3','ip1_4','ip1_port','ip2_1','ip2_2','ip2_3','ip2_4','ip2_port','anomaly']]

predict = 'anomaly'
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

model = RandomForestClassifier(n_estimators=100,max_depth=5,random_state=0,n_jobs=-1)
model.fit(X_train, y_train)

print(model)

y_pred = model.predict(X_test)

print('dlugosc'+str(len(y_pred)))
for i in range(len(y_pred)):
    if(y_pred[i] == 1):
        print("wykryto anomalie")
