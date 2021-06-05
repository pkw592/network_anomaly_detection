import keras
import pandas as pd
import numpy as np

#zaimportowanie zapisanego modelu
model = keras.models.load_model('model.h5')

#odczyt przygotowanego pliku
data = pd.read_csv('data_opt3_ready.txt', sep=';',dtype='float')

#utworzenie tablicy danych do predykcji
X = np.array(data)

#predykcja wyników
predict = model.predict(X)

#wypisywanie alertów o anomalii na podstawie przewidzianego wyniku 
#(1 - anomalia, 0 - ruch normalny)
for i in range(len(predict)):
    if(predict[i][0] != 0):
        print('Wykryto anomalie!\n')
        print('Nieautoryzowany ruch\n')
        print('Adres IP źródła:')
        print(str(int(X[i][0]))+ '.' + str(int(X[i][1])) + '.' + str(int(X[i][2])) + '.' + str(int(X[i][3])))
        print('Adres IP adresata:')
        print(str(int(X[i][5])) + '.' + str(int(X[i][6])) + '.' + str(int(X[i][7])) + '.' + str(int(X[i][8])))
        print('----------------------------------------' + '\n')
