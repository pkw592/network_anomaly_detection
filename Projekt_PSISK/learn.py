import pandas as pd
import numpy as np
from keras.layers import Embedding, SimpleRNN, Dense
from keras import Sequential

data = pd.read_csv('data_.txt', sep=';')
data = data[['ip1_1','ip1_2','ip1_3','ip1_4','anomaly']]

predict = 'anomaly'

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=256))
model.add(SimpleRNN(128))
model.add(Dense(64))
model.add(Dense(1))

#model.summary()
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
fit_model = model.fit(X, y, epochs=10, batch_size=128, validation_split=0.2)
model.save("model.h5")