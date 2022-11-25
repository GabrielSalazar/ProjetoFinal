from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd


# Delimitando tamanho do DataFrame
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)

mt5.initialize()

ticker = "IBOV"
sel = mt5.symbol_select(ticker, True)


# Resgatando do ativo selecionado, pelo timerame de 1h, 8 candles
candles = mt5.copy_rates_from(ticker, mt5.TIMEFRAME_H2, datetime.today(), 5)

data = pd.DataFrame(candles)

# Formatando o formato da hora do DataFrame
data['time'] = pd.to_datetime(data['time'], unit='s')

print(data)

mt5.shutdown()