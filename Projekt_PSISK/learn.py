import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np

data = pd.read_csv('data_all_ready.txt', sep=';',dtype="float32")

data = data[['ip1_1','ip1_2','ip1_3','ip1_4','ip1_port','ip2_1','ip2_2','ip2_3','ip2_4','ip2_port','good_or_not']]

predict = 'good_or_not'
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

for i in range(len(X)):
    X[i][0] = int(X[i][0])
    X[i][1] = int(X[i][1])
    X[i][2] = int(X[i][2])
    X[i][4] = int(X[i][8])

model = keras.Sequential()
model.add(keras.layers.Embedding(88000, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

model.summary()

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

fit_model = model.fit(X, y,epochs=50,batch_size=512)
result = model.evaluate(X,y)

print(result)

model.save('model.h5')