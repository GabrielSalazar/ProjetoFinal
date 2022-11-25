import datetime

from bus.indicators import ifr, rsl
from common.util import validate_crossover_return
from dice.alert import Alert


def validate_ifr(data_ifr, ticker, timeframe):
    alert = None
    data = ifr(data_ifr)

    data_sell = data.copy()
    data_buy = data.copy()

    #Valida se IFR cruzou 70 pra baixo
    data_sell.drop(["low_rsi"], axis=1, inplace=True)
    data_sell = data_sell.rename(columns={'IFR14': 'curta', 'high_rsi': 'longa'}, inplace=False)
    #print(data_sell)
    result = validate_crossover_return(data_sell)

    if result[0]: #result[0] == True:
        if result[1] == "SELL":
            dt = data_sell.index[len(data_sell) - 1]
            alert = Alert(dt, ticker, "", "IFR14", result[1], timeframe)
            if alert.insert() is None:
                alert = None

    #Não houve cruzamento do hight do IFR
    #Buscar então no low
    if alert is None:
        data_buy.drop(["high_rsi"], axis=1, inplace=True)
        #Valida se IFR cruzou 30 pra cima
        data_buy = data_buy.rename(columns={'IFR14': 'curta', 'low_rsi': 'longa'}, inplace=False)
        #print(data_buy)
        result = validate_crossover_return(data_buy)

        if result[0]: #result[0] == True:
            if result[1] == "BUY":
                dt = data_buy.index[len(data_buy) - 1]
                alert = Alert(dt, ticker, "", "IFR14", result[1], timeframe)
                if alert.insert() is None:
                    alert = None
    return alert



def validate_rsl(data_rsl, ticker, timeframe):
    alert = None
    data = rsl(data_rsl)

    data_sell = data.copy()
    data_buy = data.copy()

    #Valida se RSL mudou o sinal
    data_sell = data_sell.rename(columns={'RSL': 'curta', 'superior_band': 'longa'}, inplace=False)
    # print(data_sell)
    result = validate_crossover_return(data_sell)

    if result[0]: #result[0] == True:
        if result[1] == "SELL":
            alert = Alert(datetime.datetime.today(), ticker, "", "RSL", result[1], timeframe)

    # Não houve cruzamento do hight do RSL
    # Buscar então no low
    if alert is None:

        # Valida se RSL mudou pra cima
        data_buy = data_buy.rename(columns={'RSL': 'curta', 'inferior_band': 'longa'}, inplace=False)
        # print(data_buy)
        result = validate_crossover_return(data_buy)

        if result[0]: #result[0] == True:
            if result[1] == "BUY":
                alert = Alert(datetime.datetime.today(), ticker, "", "RSL", result[1], timeframe)

    return alert



#validar se o RSL continua crescendo, alta continua
#validar se o RSL continua caindo, queda continua
def validate_rsl_continue():
    pass
