import datetime
import sqlite3
from datetime import time
import pandas as pd


from bus.candle_bus import validate_candle
from bus.indicators import long_and_short_data, correlation, volume_plus_3, ifr, candle, mma
from bus.mma_bus import validate_mma
from bus.volume_bus import validate_volume, get_operation
from common.util import get_path_db
from dice.basic_load import tickers_long_and_short_corr
from dice.get_data import get_data_ticker_y
import matplotlib.pyplot as plt


def percorre():
    for par in tickers_long_and_short_corr:
        #correlation(par["long"], par["short"])
        if correlation(par["long"], par["short"]) > 0.8:
            long_and_short_data(par["long"], par["short"])
            time.sleep(10)


pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)


#print(get_data_ticker_m("BBAS3","240"))

#print(get_data_ticker_m("VALE3","240"))
#print(volume_plus_3(get_data_ticker_m('WING22','1')))
#print('-----')
#print(ifr(get_data_ticker_m('WING22','1')))

#print(get_operation(137, 29))
text = 'Python is a fun programming language'

# split the text from space
print(text.split(' ')[0])


#print(get_data_ticker_m("B3SA3", "60"))
print("--")
print("--")
print("--")
#print(get_data_ticker_y("B3SA3", "1wk"))

#print(volume_plus_3(get_data_ticker_y("PETR4", "60")))


print(ifr(get_data_ticker_y("PETR4", "60")))





#df = validate_mma(data, 'PETR4', '1wk')
#print(df)




#conn = sqlite3.connect(get_path_db())
#cur = conn.cursor()
#print(conn)
#conn.close()


#validate_candle(get_data_ticker_y('MGLU3','60'), 'MGLU3', '60')
