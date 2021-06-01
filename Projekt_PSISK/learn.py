import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.layers import Embedding, SimpleRNN, LSTM, Dense
from keras import Sequential
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = pd.read_csv('data_i2.txt', sep=';',dtype='float')

data = data[['ip1_1','ip1_2','ip1_3','ip1_4','ip1_port','ip2_1','ip2_2','ip2_3','ip2_4','ip2_port','anomaly']]

predict = 'anomaly'
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

model = Sequential()
model.add(Embedding(100000, 16))
model.add(SimpleRNN(32,activation='tanh',return_sequences=True))
model.add(Dense(1, activation='sigmoid'))

model.summary()

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

fit_model = model.fit(X, y, epochs=10, batch_size=128, validation_split=0.2)

model.save("model.h5")