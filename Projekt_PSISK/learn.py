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


data = pd.read_csv('data_csv.txt', sep=';',low_memory=False)

data = data[['ip_source','ip1_port','ip_destination','ip2_port','anomaly']]

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
model.save('model2.h5')

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("accuracy:",accuracy)
f1score=f1_score(y_test, y_pred)
print("f1-acore:",f1score)
cm=confusion_matrix(y_test, y_pred)
print("confusion matrix:\n",cm)
pr=precision_score(y_test,y_pred)
print("Precision:",pr)
rs=recall_score(y_test,y_pred)
print("Recall_score:",rs)
misclassified_samples = X_test[y_test != y_pred]
mc=misclassified_samples.shape[0]
print("Misclassified :",mc)
