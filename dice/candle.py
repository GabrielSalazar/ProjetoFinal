from common.dbase import Dbase
import pandas as pd


class Candle:

    # region data
    def __init__(self, ticker, time_frame, date_time, open, high, low, close, adj_close, volume):
        self.__ticker = ticker
        self.__time_frame = time_frame
        self.__date_time = date_time
        self.__open = open
        self.__high = high
        self.__low = low
        self.__close = close
        self.__adj_close = adj_close
        self.__volume = volume

    @property
    def ticker(self):
        return self.__ticker

    @property
    def time_frame (self):
        return self.__time_frame

    @property
    def date_time(self):
        return self.__date_time

    @property
    def open(self):
        return self.__open

    @property
    def high(self):
        return self.__high

    @property
    def low(self):
        return self.__low

    @property
    def close(self):
        return self.__close

    @property
    def adj_close(self):
        return self.__adj_close

    @property
    def volume(self):
        return self.__volume

    @ticker.setter
    def ticker(self, ticker):
        self.__ticker = ticker

    @time_frame.setter
    def time_frame(self, time_frame):
        self.__time_frame = time_frame

    @date_time.setter
    def date_time(self, date_time):
        self.__date_time = date_time

    @open.setter
    def open(self, open):
        self.__open = open

    @high.setter
    def high(self, high):
        self.__high = high

    @low.setter
    def low(self, low):
        self.__low = low

    @close.setter
    def close(self, close):
        self.__close = close

    @adj_close.setter
    def adj_close(self, adj_close):
        self.__adj_close = adj_close

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    # endregion

    # region bus

    # region pub

    def add_new_candle_d(self):
        try:
            db = Dbase()

            insert_shell = """INSERT INTO FINANCE_DATA.CANDLES_D (ticker, date_time, open, high, low, close, adj_close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

            insert_data = self.__ticker, self.__date_time, self.__open, self.__high, self.__low, self.__close, self.__adj_close, self.__volume
            return db.create(insert_shell, insert_data)

        except Exception as ex:
            print(ex)
            return False

    @staticmethod
    def read_candles_d(ticker, date_time):
        try:
            db = Dbase()

            read_shell = """SELECT * FROM FINANCE_DATA.CANDLES_D WHERE ticker = %s AND date_time >= %s"""

            read_data = ticker, date_time
            result = db.read(read_shell, read_data)
            df_result = pd.DataFrame(result, columns=['ticker', 'date_time', 'open', 'high', 'low', 'close', 'adj_close', 'volume'])

            return df_result

        except Exception as ex:
            print(ex)
            return False
    # endregion

    # region priv
    # endregion

    # endregion