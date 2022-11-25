import datetime
import time
#import MetaTrader5 as mt5
import pandas
import pandas as pd

import yfinance as yf
from common.util import get_date_minus


def delete_incomplete_candles(data):
    delete_candle = []
    found = False
    for x in range(len(data)):
        new_hour = str(data.index[x])
        new_hour = new_hour[11:16]
        if new_hour != "10:00" and found == False:
            delete_candle.append(1)
        elif new_hour == "10:00" and found == False:
            found = True
            delete_candle.append(0)
        else:
            delete_candle.append(0)

    data['delete'] = delete_candle

    data.drop(data[data['delete'] == 1].index, inplace=True)
    data.drop(["delete"], axis=1, inplace=True)

    return data


def segregate_daily_candles(data):
    candle = []

    for x in range(len(data)):
        new_hour = str(data.index[x])
        new_hour = new_hour[11:16]
        if new_hour == "10:00" or new_hour == "11:00" or new_hour == "12:00" or new_hour == "13:00":
            candle.append(10)
        else:
               candle.append(14)

    data['candle'] = candle
    return data

    #data.drop(data[data['delete'] == 1].index, inplace=True)
    #data.drop(["delete"], axis=1, inplace=True)


def calc_candle():
    pass


def create_candles_240(data):
    new_data = pd.DataFrame

    for key, value in data.iterrows():
        print(value[1])
    #for x in range(len(data)):
        #candle = data["candle"][x]
        #dt = str(data.index[x])
        #row = data.iloc[x]

        #print(dt, candle)
        #print(row)

    #print(new_data)
    #row = calc_candle(rows)
    
    return new_data



def format_timeframe240(data):

    # - Identificar o dia completo, começando pelo horário 10:00
    # - Deletar primeiros candles de 60m que não serão usandos na agregação
    data = delete_incomplete_candles(data)


    # - Separar os dois candles diários
    #   - Candle 10 (10-11, 11-12, 12-13, 13-14)
    #   - Candle 14 (14-15, 15-16, 16-17, 17-18 ou 17-17:30)
    data = segregate_daily_candles(data)

    # - Gerar novo candle (Mínima, máxima, abertura, fechamento e volume)
    data = create_candles_240(data)

    print(data)
    return data



''''
    for x in range(len(data)):
        new_hour = str(data.index[x])
        new_hour = new_hour[11:16]
        if new_hour != "10:00":
            data.drop(data.index[x], inplace=True)


    print(data)
'''




def format_timeframe120(data):

    hours_dt_120 = []
    dt_120 = []
    for x in range(len(data)):
        new_hour = str(data.index[x])
        new_hour = new_hour[11:16]
        hours_dt_120.append(new_hour)

        is_120 = 1 if new_hour == "10:00" or new_hour == "12:00" or new_hour == "14:00" or new_hour == "16:00" or new_hour == "17:30" else 0
        dt_120.append(is_120)

    data['hours'] = hours_dt_120
    data['dt_120'] = dt_120

    data.drop(data[data['dt_120'] == 0].index, inplace=True)
    data.drop(["dt_120", "hours"], axis=1, inplace=True)

    return data


#region Yahoo

def get_data_ticker_y(ticker, timeframe):
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None
    days = 0

    if str(timeframe) == "1":
        timeframe_interval = "1m"
        days = 3
    elif str(timeframe) == "5":
        timeframe_interval = "5m"
        days = 5
    elif str(timeframe) == "15":
        timeframe_interval = "15m"
        days = 10
    elif str(timeframe) == "30":
        timeframe_interval = "30m"
        days = 50
    elif str(timeframe) == "60":
        timeframe_interval = "60m"
        days = 50
    elif str(timeframe) == "90":
        timeframe_interval = "90m"
        days = 80
    elif str(timeframe) == "120":
        days = 100
    elif str(timeframe) == "1d":
        timeframe_interval = timeframe
        days = 250
    elif str(timeframe) == "1wk":
        timeframe_interval = timeframe
        days = 500

    if ticker != '^BVSP':
        if ticker != '^SPX':
            if ticker != '^IXIC':
                if ticker != '^DJI':
                    if ticker != 'GC=F':
                        if ticker != 'CL=F':
                            if ticker != 'PBR':
                                if ticker != 'VALE':
                                    if ticker != 'ITUB':
                                        if ticker != 'BBD':
                                            if ticker != 'XRP-USD':
                                                ticker = ticker + ".SA"

    days_minus = get_date_minus(days)

    # Busca no Yahoo Finance dados diários de um ativo, entre datas
    data = yf.download(ticker, start = days_minus, end = datetime.datetime.today(), progress = False, interval = timeframe_interval)
    
    if timeframe == "120":
        data = format_timeframe120(data)

    return data


def get_data_ticker(ticker, timeframe):
    pass

def get_data_ticker_y_day(ticker, days):
    ticker = ticker + ".SA"
    days_minus = get_date_minus(days)
    data = yf.download(ticker, start=days_minus, end=datetime.datetime.today(), progress=False)
    return data

#endregion

#region MetaTrader
''''
def get_data_ticker_m(ticker, timeframe):
    try:
        mt5.initialize()

        qtde_candles = 200
        #if timeframe.isnumeric():
        #    if int(timeframe) == 240:
        #        qtde_candles = 400

        if str(timeframe) == "1":
            timeframe_interval = mt5.TIMEFRAME_M1
        elif str(timeframe) == "2":
            timeframe_interval = mt5.TIMEFRAME_M2
        elif str(timeframe) == "4":
            timeframe_interval = mt5.TIMEFRAME_M4
        elif str(timeframe) == "5":
            timeframe_interval = mt5.TIMEFRAME_M5
        elif str(timeframe) == "15":
            timeframe_interval = mt5.TIMEFRAME_M15
        elif str(timeframe) == "30":
            timeframe_interval = mt5.TIMEFRAME_M30
        elif str(timeframe) == "60":
            timeframe_interval = mt5.TIMEFRAME_H1
        elif str(timeframe) == "90":
            timeframe_interval = mt5.TIMEFRAME_H1
        elif str(timeframe) == "120":
            timeframe_interval = mt5.TIMEFRAME_H2
        elif str(timeframe) == "240":
            timeframe_interval = mt5.TIMEFRAME_H4
        elif str(timeframe) == "1d":
            timeframe_interval = mt5.TIMEFRAME_D1
        elif str(timeframe) == "1w":
            timeframe_interval = mt5.TIMEFRAME_W1


        if ticker == '^BVSP':
            ticker = 'IBOV'

        sel = mt5.symbol_select(ticker, True)

        # Resgatando do ativo selecionado, pelo timerame de 1h, 8 candles
        candles = mt5.copy_rates_from(ticker, timeframe_interval, datetime.datetime.today(), qtde_candles)

        data = pd.DataFrame(candles)
        #print(data)
        # Formatando o formato da hora do DataFrame
        data['time'] = pd.to_datetime(data['time'], unit='s')

        data.drop(['tick_volume', 'spread'], axis=1, inplace=True)
        data = data.rename(columns={'time': 'Datetime','open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Adj Close',
                                    'real_volume': 'Volume'}, inplace=False)
        #data = data.rename(columns={'time': 'Datetime', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Adj Close',
        #                            'real_volume': 'Volume'}, inplace=False)
        data['Close'] = data['Adj Close']

        #data = data.pd.DataFrame.set_index('Datetime')
        data = data.set_index('Datetime')

        #if timeframe == "240":
        #    data = format_timeframe240(data)

    except Exception as e:
        print("Erro carregar dados " + ticker)
        print(e)
    finally:
        mt5.shutdown()
        return data

#endregion
'''


#-------------------------------------------- test
#print(get_data_ticker_y_day("CSNA3", 10))

