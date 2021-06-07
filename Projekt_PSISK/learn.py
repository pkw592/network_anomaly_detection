import pandas as pd
import numpy as np
from keras.layers import Embedding, SimpleRNN, Dense
from keras import Sequential


#wczytanie pliku do nauki modelu
data = pd.read_csv('data_i2.txt', sep=';',dtype='float')

#wczytanie danych ze względu na nagłówek kolumny
data = data[['ip1_1','ip1_2','ip1_3','ip1_4','ip1_port','ip2_1','ip2_2','ip2_3','ip2_4','ip2_port','anomaly']]

#utworzenie zmiennej zawierającej dane czy ruch jest właściwy
predict = 'anomaly'

#utworzenie tablic danych do uczenia i wyników
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

#utworzenie modelu używającego algorytmu prostych rekurencyjnych sieci neuronowych
model = Sequential()
model.add(Embedding(100000, 16))
model.add(SimpleRNN(32,activation='tanh',return_sequences=True))
model.add(Dense(1, activation='sigmoid'))

model.summary()

#kompilacja modelu
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

#uczenie modelu
fit_model = model.fit(X, y, epochs=10, batch_size=128, validation_split=0.2)

#zapis modelu do pliku
#model.save("model.h5")