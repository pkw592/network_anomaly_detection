import keras
import pandas as pd
import numpy as np

model = keras.models.load_model('model.h5')

data = pd.read_csv('data_opt3_ready.txt', sep=';',dtype='float32')

X = np.array(data)

predict = model.predict(X)
print(predict)
for i in range(len(predict)):
    if(predict[i][0]>1.1):
        print('Wykryto anomalie!\n')
        print('Adres IP źródła:')
        print(int(X[i][0])+ '.' + int(X[i][1]) + '.' + int(X[i][2]) + '.' + int(X[i][3]))
        print(' Na porcie:' + int(X[i][4]) + '\n')
        print('Adres IP adresata:')
        print(int(X[i][5])+ '.' + int(X[i][6]) + '.' + int(X[i][7]) + '.' + int(X[i][8]))
        print(' Na porcie:' + int(X[i][10]) + '\n')
