import keras
import pandas as pd
import numpy as np

#zaimportowanie zapisanego modelu
model = keras.models.load_model('model.h5')

#odczyt przygotowanego pliku
data = pd.read_csv('bad.txt', sep=';')

#wczytanie danych ze względu na nagłówek kolumny
data = data[['ip1_1','ip1_2','ip1_3','ip1_4','anomaly']]

#utworzenie zmiennej zawierającej dane czy ruch jest właściwy
predict = 'anomaly'

#utworzenie tablic danych do uczenia i wyników
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

#usuwanie powtarzających się danych
model = model.fit(X, y, epochs=10, batch_size=128, validation_split=0.2)

#zapis dotrenowanego modelu do pliku
model.save("model.h5")