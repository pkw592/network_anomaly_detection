import keras
import pandas as pd
import numpy as np

#zaimportowanie zapisanego modelu
model = keras.models.load_model('model.h5')

#odczyt przygotowanego pliku
data = pd.read_csv('data_test.txt', sep=';')

#usuwanie powtarzających się danych
data = data.drop_duplicates(['ip1_1','ip1_2','ip1_3','ip1_4'])

#utworzenie tablicy danych do predykcji
X = np.array(data)

#predykcja wyników
predict = model.predict(X)
print(predict)

#wypisywanie alertów o anomalii na podstawie przewidzianego wyniku 
#(1 - anomalia, 0 - ruch normalny)
for i in range(len(predict)):
    if(predict[i][0] <= 1):
        print('\nWykryto anomalie!\n')
        print('Nieautoryzowany ruch\n')
        print('Adres IP źródła:')
        print(str(int(X[i][0]))+ '.' + str(int(X[i][1])) + '.' + str(int(X[i][2])) + '.' + str(int(X[i][3])))
        print('----------------------------------------' + '\n')
