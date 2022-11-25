import datetime
import yfinance as yf
import pandas as pd
import numpy as np


# Busca no Yahoo Finance dados diários de um ativo, entre datas
data = yf.download("IRBR3.SA", start= datetime.datetime.today(), end= datetime.datetime.today(), progress=False)

print(data)

# Cria um novo Data Frame com a data do primeiro data frame como primeiro campo
data_signal = pd.DataFrame(index = data.index)

# Adiciona a coluna Close ao novo Data Frame
data_signal['price'] = data['Close']

# Adiciona a coluna diff realizando o cálculo de diferença entre linhas da colina price
data_signal['diff'] = data_signal['price'].diff()

# Adiciona a coluna signal
data_signal['signal'] = 0.0

# Realiza o cálculo condicional de diferença da coluna signal. Se a diferença entre linas da coluna diff é 0 então é 1, se não 0
data_signal['signal'] = np.where(data_signal['diff'] > 0.0, 1.0, 0.0)

# Cria colina position com a diferença da coluna signal
data_signal['position'] = data_signal['signal'].diff()

initial_capital = 1000.0

# Cria novos Data Frames para cálculo
positions = pd.DataFrame(index = data_signal.index).fillna(0.0)
portfolio = pd.DataFrame(index = data_signal.index).fillna(0.0)


# Set coluna do ativo
positions['PETR4'] = data_signal['signal']

# Cálculo de backtesting
portfolio['positions'] = (positions.multiply(data_signal['price'], axis = 0)).cumsum()
portfolio['cash'] = initial_capital -  (positions.diff().multiply(data_signal['price'], axis = 0)).cumsum()

# Consolidação do resultado
portfolio['total'] = portfolio['positions'] + portfolio['cash']

print(data_signal)

print(portfolio)
