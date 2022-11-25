import math
import numpy as np
import ta
from ta.volume import ChaikinMoneyFlowIndicator

from common.util import get_date_minus

from dice.get_data import get_data_ticker_y, get_data_ticker_y_day
import pandas as pd

import yfinance as yf


#region MMA

def mma(data):

    data['mma9'] = data['Adj Close'].rolling(9).mean()
    data['mma21'] = data['Adj Close'].rolling(21).mean()
    data['mma50'] = data['Adj Close'].rolling(50).mean()

    data.drop(['Open', 'High', 'Low', 'Close', "Volume"], axis=1, inplace=True)
    data.dropna(inplace=True)
    return data

#endregion


#region Bollinger IFR RSI RSL STOCH
def bollinger(data):

    periodos= 20
    desvios = 2

    data['desvio'] = data['Adj Close'].rolling(periodos).std()
    data['mm'] = data['Adj Close'].rolling(periodos).mean()

    data['inferior_band'] = data['mm'] - (data['desvio'] * desvios)
    data['superior_band'] = data['mm'] + (data['desvio'] * desvios)

    data.drop(['Open', 'High', 'Low', 'Close', "Volume", "desvio", "mm"], axis=1, inplace=True)
    data.dropna(inplace=True)

    #data.plot()
    #plt.show()
    return


def ifr(data):
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    rsi14 = ta.momentum.RSIIndicator(close = data["Adj Close"], window = 14, fillna = False)
    #rsi14
    data["IFR14"] = rsi14.rsi()

    data.drop(['Open', 'High', 'Low', 'Close', "Volume", "Adj Close"], axis=1, inplace=True)
    #data.dropna(inplace=True)

    data['high_rsi'] = 70
    data['low_rsi'] = 30

    return data



def rsl(data):
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    periodos = 9

    data['mm'] = data['Adj Close'].rolling(periodos).mean()
    data['RSL'] = (data['Adj Close'] / data['mm'] - 1) * 100
    #data['change'] = 0


    periodos = 9
    desvios = 2


    data['mm_detrand'] = data['RSL'].rolling(periodos).mean()
    data['afastamento'] = data['RSL'] - data['mm_detrand']
    data['mm_afastamento'] = data['afastamento'].mean()

    data['desvio'] = data['afastamento'].std()

    data['inferior_band'] = data['mm_afastamento'] - (data['desvio'] * desvios)
    data['superior_band'] = data['mm_afastamento'] + (data['desvio'] * desvios)



    data.drop(['Open', 'High', 'Low', 'Close', "Volume", "mm", "Adj Close" , "mm_detrand", "desvio", "mm_afastamento" , "afastamento"], axis=1, inplace=True)
    data.dropna(inplace=True)

    return data


def stoch(data):

#Stochastic Oscillator
#ref: https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html?highlight=stoch#ta.momentum.stoch
#signature: ta.momentum.stoch(high, low, close, window=14, smooth_window=3, fillna=False) → pandas.core.series.Series

    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    obj_stoch = ta.momentum.StochasticOscillator(close = data["Adj Close"],high = data["High"], low = data["Low"], window=14, smooth_window=3, fillna = False)
    #rsi14
    data["stoch"] = obj_stoch.stoch()

    #data.drop(['Open', 'High', 'Low', "Volume", "Adj Close"], axis=1, inplace=True)
    #data.dropna(inplace=True)

    #data['high_stoch'] = 80
    #data['low_stoch'] = 20

    return data

#endregion


#region Volume

def volume_plus(data):
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    periodos = 10

    data['mm'] = data['Volume'].rolling(periodos).mean()
    data['afastamento'] = data['Volume'] - data['mm']
    data['percentage'] = (data['afastamento'] / data['mm']) * 100

    #data['desvio'] = data['afastamento'].std()

    #data['inferior_band'] = data['mm_afastamento'] - (data['desvio'] * desvios)
    #data['superior_band'] = data['mm_afastamento'] + (data['desvio'] * desvios)

    data.drop(['Open', 'High', 'Low', 'Close',"Adj Close", "Volume", "mm", "afastamento"], axis=1, inplace=True)
    data.dropna(inplace=True)

    #print(inferior_band)
    #print(superior_band)
    #print(data)
    return data


def volume_plus_2(data):
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    periodos = 8
    data.drop(data[data['Volume'] == 0].index, inplace=True)
    data['Var Volume'] = data['Volume'].pct_change() * 100
    data['desvio'] = data['Volume'].rolling(periodos).std()
    data['mm'] = data['Volume'].rolling(periodos).mean()

    data['desvio_3'] = data['mm'] + (data['desvio'] * 2)

    data.drop(['Open', 'High', 'Low', 'Close', 'Adj Close', 'desvio', 'mm', 'desvio_3'], axis=1, inplace=True)

    data.dropna(inplace=True)
    #print(inferior_band)
    #print(superior_band)
    #print(data)
    return data


def volume_plus_3(data):

    periodos = 60
    #data.drop(data[data['Volume'] == 0].index, inplace=True)
    data.dropna(inplace=True)

    data['mm'] = data['Volume'].rolling(periodos).mean()

    cor_candle = []
    percent = []
    for ind in data.index:
        perc = ((data['Volume'][ind] / data['mm'][ind]) - 1) * 100

        if data['Volume'][ind] > data['mm'][ind]:
            if 100 < perc < 150:
                cor = 'AMARELO'
            elif perc >= 150:
                cor = 'VERMELHO'
            else:
                cor = "BRANCO"
        else:
            #perc = 0
            if math.isnan(perc):
                perc = 0
            cor = 'BRANCO'
        cor_candle.append(cor)
        percent.append(perc)

    data['cor_candle'] = cor_candle
    data['percent'] = percent
    data.drop(['mm'], axis=1, inplace=True)


    #print(data)
    return data


def cmf(data):
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    chaikin = ta.volume.ChaikinMoneyFlowIndicator(high = data["High"], low = data["Low"], close = data["Adj Close"], volume = data["Volume"], window = 21, fillna = False)
    data["zero"] = 0
    data["CMF"] = chaikin.chaikin_money_flow()

    periodos = 20
    desvios = 2

    data['mm'] = data['CMF'].rolling(periodos).mean()
    data['afastamento'] = data['CMF'] - data['mm']
    data['mm_afastamento'] = data['afastamento'].mean()

    data['desvio'] = data['afastamento'].std()

    data['inferior_band'] = data['mm_afastamento'] - (data['desvio'] * desvios)
    data['superior_band'] = data['mm_afastamento'] + (data['desvio'] * desvios)


    data.drop(['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close', 'mm', 'afastamento', 'mm_afastamento', 'desvio'], axis=1, inplace=True)
    data.dropna(inplace=True)

    return data

#endregion


#region Retorno diários
def daily_return(ticker):
    data = get_data_ticker_y_day(ticker, 10)
    data['daily_retun'] = data['Adj Close'].pct_change() * 100

    #data['desvio'] = data['afastamento'].std()

    #data['inferior_band'] = data['mm_afastamento'] - (data['desvio'] * desvios)
    #data['superior_band'] = data['mm_afastamento'] + (data['desvio'] * desvios)

    data.drop(['Open', 'High', 'Low', 'Close', "Volume"], axis=1, inplace=True)
    data.dropna(inplace=True)


    #print(inferior_band)
    #print(superior_band)
    return data
#endregion


#region Long and Short

def correlation(ticker_buy, ticker_sell):
    data = get_data_ticker_y_day(ticker_buy, 30)
    data['daily_retun_buy'] = data['Adj Close'].pct_change() * 100


    data2 = get_data_ticker_y_day(ticker_sell, 30)
    data2['daily_retun_sell'] = data2['Adj Close'].pct_change() * 100
    # data['desvio'] = data['afastamento'].std()

    # data['inferior_band'] = data['mm_afastamento'] - (data['desvio'] * desvios)
    # data['superior_band'] = data['mm_afastamento'] + (data['desvio'] * desvios)

    data.drop(['Open', 'High', 'Low', 'Close', "Volume", "Adj Close"], axis=1, inplace=True)
    data.dropna(inplace=True)
    data2.dropna(inplace=True)

    data["daily_retun_sell"] = data2["daily_retun_sell"]

    corr = data["daily_retun_buy"].corr(data["daily_retun_sell"])


    # print(inferior_band)
    # print(superior_band)
    #print(data)
    #print(ticker_buy + " vs " + ticker_sell + " - " + str(corr))
    return corr


def long_and_short_data(ticker_buy, ticker_sell):

    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    buy = get_data_ticker_y_day(ticker_buy, 100)
    sell = get_data_ticker_y_day(ticker_sell, 100)

    df = buy
    df['buy'] = buy['Adj Close']


    df['sell'] = sell['Adj Close']
    df['ratio'] = df['buy'] / df['sell']
    df['mma20'] = df['ratio'].rolling(20).mean()

    df['desvio'] = df['ratio'].rolling(20).std()

    df['inferior_band'] = df['mma20'] - (df['desvio'] * 2)
    df['superior_band'] = df['mma20'] + (df['desvio'] * 2)


    df.dropna(inplace=True)
    df.drop(['Open', 'High', 'Low', 'Close', "Volume", 'Adj Close', 'desvio', 'buy', 'sell'], axis=1, inplace=True)

    #df.plot()
    #plt.title(ticker_buy + " vs " + ticker_sell)
    #plt.show()
    #print(df)
    return df

#endregion


#region Volatilidade

def mom(data):
    #data["mom"] = (data["Adj Close"].rolling(10).meam() - data["Adj Close"]) * 100

    data["mom_shift"] = data["Adj Close"]
    data["mom_shift"] = data["mom_shift"].shift(13, axis = 0)
    data["mom"] = (data["mom_shift"] - data["Adj Close"]) * 100

    periodos = 9
    desvios = 2


    data['mm'] = data['mom'].rolling(periodos).mean()
    data['afastamento'] = data['mom'] - data['mm']
    data['mm_afastamento'] = data['afastamento'].mean()

    data['desvio'] = data['afastamento'].std()

    data['inferior_band'] = data['mm_afastamento'] - (data['desvio'] * desvios)
    data['superior_band'] = data['mm_afastamento'] + (data['desvio'] * desvios)
    #data['zero'] = 0



    data.drop(['Open', 'High', 'Low', 'Close', "Volume", 'mom_shift', 'Adj Close', 'mm_afastamento', 'mm', 'desvio', 'afastamento'], axis=1, inplace=True)
    data.dropna(inplace=True)

    return data


def historical_volatility(ticker):
    data = get_data_ticker_y_day(ticker, 100)

    data["Log Return"] = np.log(data["Adj Close"] / data["Adj Close"].shift(1))
    data["volatility"] = data["Log Return"].rolling(20).std() * np.sqrt(252)
    data.drop(['Open', 'High', 'Low', 'Close', "Volume", "Log Return"], axis=1, inplace=True)
    data.dropna(inplace=True)

    return data


def vol_index_detrand(data):
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    periodos = 20
    desvios = 2



    data['mm'] = data['Adj Close'].rolling(periodos).mean()
    data['afastamento'] = data['Adj Close'] - data['mm']
    data['mm_afastamento'] = data['afastamento'].mean()

    data['desvio'] = data['afastamento'].std()

    data['inferior_band'] = data['mm_afastamento'] - (data['desvio'] * desvios)
    data['superior_band'] = data['mm_afastamento'] + (data['desvio'] * desvios)

    data.drop(['Open', 'High', 'Low', 'Close',"Adj Close", "mm", 'desvio', "Volume"], axis=1, inplace=True)
    data.dropna(inplace=True)


    #print(inferior_band)
    #print(superior_band)
    #data.plot()
    #plt.show()

    return data


def mvrv():
    pass


def implied_volatility(ticker):
    pass


def compare_implied_historical_volatility(ticker):
    pass


def candle(data):

    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    data["amplitude"] = data["High"] - data["Low"]
    data["bulk"] = data["Adj Close"] - data["Open"]

    data = get_top_wick(data)
    data = get_bottom_wick(data)
    data = get_percents(data)
    return data




def get_top_wick(data):
    top_wick_list = []

    for ind in data.index:
        if data["bulk"][ind] > 0:
            top_wick = data["High"][ind] - data["Adj Close"][ind]
        else:
            top_wick = data["High"][ind] - data["Open"][ind]

        top_wick_list.append(top_wick)

    data['top_wick'] = top_wick_list
    return data


def get_bottom_wick(data):
    bottom_wick_list = []

    for ind in data.index:
        # Calcula o pavio inferior
        if data["bulk"][ind] > 0:
            bottom_wick = data["Low"][ind] - data["Open"][ind]
        else:
            bottom_wick = data["Low"][ind] - data["Adj Close"][ind]

        bottom_wick_list.append(bottom_wick)

    data['bottom_wick'] = bottom_wick_list
    return data



def get_percents(data):
    percent_bulk_list = []
    percent_top_wick_list = []
    percent_bottom_wick_list = []

    for ind in data.index:

        # Calcula o % da massa, do body do candle
        if data["bulk"][ind] < 0:
            percent_bulk = (data["bulk"][ind] * -1) / data["amplitude"][ind]
        else:
            percent_bulk = data["bulk"][ind] / data["amplitude"][ind]

        # Calcula o % do pavio superior
        if data["top_wick"][ind] < 0:
            percent_top_wick = (data["top_wick"][ind] * -1) / data["amplitude"][ind]
        else:
            percent_top_wick = data["top_wick"][ind] / data["amplitude"][ind]

        # Calcula o % do pavio superior
        if data["bottom_wick"][ind] < 0:
            percent_bottom_wick = (data["bottom_wick"][ind] * -1) / data["amplitude"][ind]
        else:
            percent_bottom_wick = data["bottom_wick"][ind] / data["amplitude"][ind]

        percent_bulk_list.append(percent_bulk)
        percent_top_wick_list.append(percent_top_wick)
        percent_bottom_wick_list.append(percent_bottom_wick)

    data['percent_bulk'] = percent_bulk_list
    data['percent_top_wick'] = percent_top_wick_list
    data['percent_bottom_wick'] = percent_bottom_wick_list
    return data

#endregion




#------------------------------------------test

mvrv()

#data = get_data_ticker_y("USIM5", "120")
#print(mma(data))


#data = rsl("GGBR4", "1d")
#data.drop(['Open', 'High', 'Low', 'Close', "Volume", "mm"], axis=1, inplace=True)
#data.dropna(inplace=True)
#print(data)

#correlation("VALE3", "USIM5")
#long_and_short_data("BBDC4", "ITUB4")
#percorre()


#price_vol_detrand("BBDC4", "1d")

#volume_plus("CSNA3", "1d")
#print(historical_volatility("BBDC4"))
#print(daily_return("CSNA3"))