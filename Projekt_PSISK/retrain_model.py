import keras
import pandas as pd
import numpy as np

model = keras.models.load_model('model.h5')

data = pd.read_csv('bad.txt', sep=';')
data = data[['ip1_1','ip1_2','ip1_3','ip1_4','anomaly']]
predict = 'anomaly'

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

model = model.fit(X, y, epochs=10, batch_size=128, validation_split=0.2)
model.save("model.h5")