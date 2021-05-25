import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np

data = pd.read_csv('data_all.txt', sep=';')

data = data[['ip1','ip2','type','good_or_not']]

predict = 'good_or_not'

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])
print(X)
X = pd.get_dummies(X)
print(X)
X = keras.utils.to_categorical(X,num_classes=None,dtype='float32')
print(X)

model = keras.Sequential()
model.add(keras.layers.Embedding(88000, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

model.summary()

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

fit_model = model.fit(X, y,epochs=10,batch_size=512)
result = model.evaluate(X,y)

print(result)

model.save('model.h5')