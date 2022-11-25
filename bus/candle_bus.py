import datetime
import time

from bus.indicators import candle, ifr
from dice.alert import Alert


def validate_candle(data, ticker, timeframe):
    alert = None
    data_valid = candle(data)


    new_data_valid = data_valid.copy()
    i_list = get_ifr_df(ifr(data_valid))

    new_data_valid['IFR14'] = i_list

    if len(new_data_valid) > 0:
        oper = "NONE"

        new_data_valid = new_data_valid.tail(2).head(1)
        percent_top_wick = new_data_valid.iat[0,11]
        percent_bottom_wick = new_data_valid.iat[0,12]

        dt = new_data_valid.index[len(new_data_valid) - 1]
        ifr_value = new_data_valid.iat[0, 13]


        if percent_bottom_wick >= 0.5 and round(ifr_value, 0) <= 35:
            oper = "BUY"
            pavio = percent_bottom_wick
        elif percent_top_wick >= 0.5 and round(ifr_value, 0) >= 65:
            oper = "SELL"
            pavio = percent_top_wick


        print('Pavio inferior: ' + str(percent_bottom_wick))
        print('Pavio superior: ' + str(percent_top_wick))
        print('IFR 14: ' + str(round(ifr_value, 0)))
        time.sleep(1)


        if oper != "NONE":
            alert = Alert(dt, ticker, "", "CANDLE", str(oper + ' - ' + 'IFR14: ' + str(round(ifr_value, 0)) + ' - PAVIO: ' + str(pavio) + '%'), str(timeframe))
            if alert.insert() is None:
                alert = None
        else:
            alert is None
    return alert



def get_ifr_df(data):
    ifr_list = []
    for i in range(0, len(data)):
        ifr_list.append(data.iloc[i]['IFR14'])

    #print(len(ifr_list))
    return ifr_list