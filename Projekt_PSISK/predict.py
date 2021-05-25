import keras
import pandas as pd
import numpy as np

model = keras.models.load_model('model.h5')

data = pd.read_csv('data_opt3.txt', sep=';')

data = data[['ip1','ip2','type']]

X = np.array(data)
X = keras.utils.to_categorical(X,num_classes=None,dtype='float32')
print(X)

#predict = 