import pandas as pd
import numpy as np
from keras.layers import Embedding, SimpleRNN, Dense, GRU
from keras import Sequential

#wczytanie pliku do nauki modelu
data = pd.read_csv('data_.txt', sep=';')

#wczytanie danych ze względu na nagłówek kolumny
data = data[['ip1_1','ip1_2','ip1_3','ip1_4','anomaly']]

#utworzenie zmiennej zawierającej dane czy ruch jest właściwy
predict = 'anomaly'

#utworzenie tablic danych do uczenia i wyników
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

#utworzenie modelu używającego algorytmu prostych rekurencyjnych sieci neuronowych
model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=256))
model.add(SimpleRNN(128))
model.add(Dense(64))
model.add(Dense(1))

#model.summary()

#kompilacja modelu
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

#uczenie modelu
fit_model = model.fit(X, y, epochs=10, batch_size=128, validation_split=0.2)

#zapis modelu do pliku
model.save("model.h5")