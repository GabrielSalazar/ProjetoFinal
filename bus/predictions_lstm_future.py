import math
import numpy
from keras.models import Sequential
from keras.layers import Dense, LSTM
from dice.get_data import get_data_ticker_y, get_data_ticker_m
import pandas as pd
import numpy as np
from numpy import array
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def create_dataset(dataset, time_step = 1):
    data_x, data_y = [], []
    for i in range(len(dataset)-time_step-1):
        a = dataset[i:(i+time_step), 0]
        data_x.append(a)
        data_y.append(dataset[i + time_step, 0])
    return numpy.array(data_x), numpy.array(data_y)

df = get_data_ticker_y("XRP-USD","1d")
df1 = df.reset_index()['Adj Close']

#plt.plot(df1)
#plt.show()

scaler = MinMaxScaler(feature_range=(0, 1))
df1 = scaler.fit_transform(np.array(df1).reshape((-1, 1)))

training_size = int(len(df1) * 0.7)
test_size = len(df) - training_size
train_data, test_data = df1[0:training_size, :], df1[training_size: len(df1), :1]

time_step = 100
x_train, y_train = create_dataset(train_data, time_step)
x_test, y_test = create_dataset(test_data, time_step)

x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(100,1)))
model.add(LSTM(50, return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100, batch_size=64, verbose=1)

train_predict = model.predict(x_train)
test_preditct = model.predict(x_test)

train_predict = scaler.inverse_transform(train_predict)
test_preditct = scaler.inverse_transform(test_preditct)

math.sqrt(mean_squared_error(y_train, train_predict))
math.sqrt(mean_squared_error(y_test, test_preditct))

look_back = 100
train_predict_plot = numpy.empty_like(df1)
train_predict_plot[:, :] = np.nan
train_predict_plot[look_back:len(train_predict)+look_back, :] = train_predict

test_preditct_plot = numpy.empty_like(df1)
test_preditct_plot[:, :] = numpy.nan
test_preditct_plot[len(train_predict)+(look_back*2)+1: len(df1)-1, :] = test_preditct

#plt.plot(scaler.inverse_transform(df1))
#plt.plot(train_predict_plot)
#plt.plot(test_preditct_plot)
#plt.show()

x_input = test_data[(len(test_data) - 100):].reshape(1, -1)

temp_input = list(x_input)
temp_input = temp_input[0].tolist()

lst_output = []

n_steps = 100
i = 0
while i < 30:
    if len(temp_input) > 100:
        x_input = np.array((temp_input[1:]))
        x_input = x_input.reshape(1,-1)
        x_input = x_input.reshape((1, n_steps, 1))
        yhat = model.predict(x_input, verbose=0)
        temp_input.extend(yhat[0].tolist())
        temp_input = temp_input[1:]
        lst_output.extend(yhat.tolist())
        i = i + 1
    else:
        x_input = x_input.reshape(1, n_steps, 1)
        yhat = model.predict(x_input, verbose = 0)
        temp_input.extend(yhat[0].tolist())
        lst_output.extend(yhat.tolist())
        i = i + 1

day_new = np.arange(1,101)
day_pred = np.arange(101,131)

df3 = df1.tolist()
df3.extend(lst_output)

print(day_new)
print(scaler.inverse_transform(df1[len(df1)-100 :]))

plt.plot(day_new, scaler.inverse_transform(df1[len(df1)-100 :]))
plt.plot(day_pred, scaler.inverse_transform(lst_output))
plt.show()







