import keras
import pandas as pd
import numpy as np

model = keras.models.load_model('model.h5')

data = pd.read_csv('data_opt3_ready.txt', sep=';',dtype='float')

X = np.array(data)

predict = model.predict(X)
print(predict)

for i in range(len(predict)):
    if(predict[i][0] != 0):
        print('Wykryto anomalie!\n')
        print('Nieautoryzowany ruch\n')
        print('Adres IP źródła:')
        print(str(int(X[i][0]))+ '.' + str(int(X[i][1])) + '.' + str(int(X[i][2])) + '.' + str(int(X[i][3])))
        print('Adres IP adresata:')
        print(str(int(X[i][5])) + '.' + str(int(X[i][6])) + '.' + str(int(X[i][7])) + '.' + str(int(X[i][8])))
        print('----------------------------------------' + '\n')
