from math import tanh
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.layers import Dense
from sklearn.model_selection import train_test_split


data = pd.read_csv('data_i1_heh.txt', sep=';',dtype="float32")

data = data[['ip1','ip1_port','ip2','ip2_port','good_or_not']]

predict = 'good_or_not'
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

model = keras.Sequential()
model.add(Dense(units=122,kernel_initializer='uniform',activation='relu'))
model.add(Dense(units=122,kernel_initializer='uniform',activation='relu'))
model.add(Dense(units=122,kernel_initializer='uniform',activation='relu'))
model.add(Dense(units=122,kernel_initializer='uniform',activation='relu'))
model.add(Dense(units=1,kernel_initializer='uniform',activation='sigmoid'))

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

fit_model = model.fit(X, y,epochs=10,batch_size=512)

#fit_model = model.fit(X, y,epochs=10,batch_size=512)
result = model.evaluate(X,y)

print(result)

model.save('model2.h5')