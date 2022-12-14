import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt

from dice.get_data import get_data_ticker_y, get_data_ticker_m
plt.style.use('fivethirtyeight')

df_data = get_data_ticker_y("PETR4","1d")

#print(df_data)

#plt.figure(figsize=(16,8))
#plt.title('Close Price History')
#plt.plot(df_data['Close'])
#plt.xlabel('Date', fontsize=20)
#plt.ylabel('Close Price R$', fontsize=20)
#plt.show()

#Create a new dataframe with only the Close Column
df_close = df_data.filter(['Close'])

#Convert the dataframe to a numpy array
dataset = df_close.values

#Get the number of rows to tran the model on
training_df_close_len = math.ceil( len( dataset)  * .8)
#print(training_df_close_len)

#Scale the data df_close
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

#print(scaled_data)

#Create training data set
#Create the scaled training data set
train_data = scaled_data[0:training_df_close_len, :]

#Split the data into x_train and y_train data sets
x_train = []
y_train = []

#here is 60
for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i,0])

    #if  i <= 61:
    #    print(x_train)
    #    print(y_train)
    #    print()

#Convert the x_train and y_train tu numpy arrays
x_train, y_train = np.array(x_train), np.array(y_train)

#Reshape the data
x_train = np.reshape(x_train,(x_train.shape[0], x_train.shape[1], 1))

#Build the LSTM Model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))

model.add(Dense(25))
model.add(Dense(1))

#Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

#Train the model

model.fit(x_train, y_train, batch_size=1, epochs=1)

#Create the testing data set
#Create a new array containg scaled values from index 1543 to 2003 = 60 ;)
test_data = scaled_data[training_df_close_len - 60: , :]

#Create the data sets x_test and y_test
x_test = []
y_test = dataset[training_df_close_len: , :]

for i in range(60, len(test_data)):
    x_test.append((test_data[i-60:i, 0]))

#Convert the data to numpy array
x_test = np.array(x_test)

#Reshape the data
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

#Get the model predicted price values
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

#Get the root mean squared error (RMSE)
rmse = np.sqrt( np.mean(predictions - y_train) **2 )
#print(rmse)

#Plot the data
train = df_close[:training_df_close_len]
valid = df_close[training_df_close_len:]
valid['Predictions'] = predictions

plt.figure(figsize=(16,8))
plt.title('Model LSTM')
plt.xlabel('Date', fontsize=20)
plt.ylabel('Predictions Close Price R$', fontsize=20)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()


