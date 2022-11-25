import sqlite3

from common.util import get_path_db


class RedCandle:

    def __init__(self, current_date, ticker, volume, percent, low, high, stoch_red_candle, oper, time_frame, alarmed):
        self.__current_date = current_date
        self.__ticker = ticker
        self.__volume = volume
        self.__percent = percent
        self.__low = low
        self.__high = high
        self.__stoch_red_candle = stoch_red_candle
        self.__oper = oper
        self.__time_frame = time_frame
        self.__alarmed = alarmed

    @property
    def current_date(self):
        return self.__current_date

    @property
    def ticker(self):
        return self.__ticker

    @property
    def volume(self):
        return self.__volume

    @property
    def percent(self):
        return self.__percent

    @property
    def low(self):
        return self.__low

    @property
    def high(self):
        return self.__high

    @property
    def stoch_red_candle(self):
        return self.__stoch_red_candle

    @property
    def oper(self):
        return self.__oper

    @property
    def time_frame(self):
        return self.__time_frame


    @property
    def alarmed(self):
        return self.__alarmed

    @current_date.setter
    def current_date(self, current_date):
        self.__current_date = current_date

    @ticker.setter
    def ticker(self, ticker):
        self.__volume = ticker

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @percent.setter
    def percent(self, percent):
        self.__percent = percent

    @high.setter
    def high(self, high):
        self.__hight = high

    @low.setter
    def low(self, low):
        self.__low = low

    @stoch_red_candle.setter
    def stoch_red_candle(self, stoch_red_candle):
        self.__stoch_red_candle = stoch_red_candle

    @oper.setter
    def oper(self, oper):
        self.__oper = oper


    @time_frame.setter
    def time_frame(self, time_frame):
        self.__time_frame = time_frame

    @alarmed.setter
    def alarmed(self, alarmed):
        self.__alarmed = alarmed

    def insert(self):
        try:

            if self.__validate_between_old_red_candle():

                conn = sqlite3.connect(get_path_db())
                cur = conn.cursor()
                alarmed = 0
                values = (
                    self.__current_date.day,
                    self.__current_date.month,
                    self.__current_date.year,
                    str(self.__current_date)[11:16],
                    self.__ticker,
                    self.__volume,
                    self.__percent,
                    self.__low,
                    self.__high, self.__stoch_red_candle, self.__oper, self.__time_frame, alarmed)
                sql = 'insert into red_candle (current_date_day, ' \
                      'current_date_month, ' \
                      'current_date_year, ' \
                      'current_date_time, ' \
                      'ticker, ' \
                      'volume, ' \
                      'percent, ' \
                      'low, high, stoch, oper, time_frame, alarmed) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
                ret = cur.execute(sql, values)
                conn.commit()
                conn.close()
        except Exception as e:
            print(
                "Volueme Ticker: " + self.__ticker + " repetido")
            print(e)
            ret = None
        finally:
            print("-")
            print("NOVO CANDLE CADASTRADO TICKER: " + self.__ticker + " - VOLUME: " + str(self.__volume) + " - VARIAÇÃO: " + str(self.__percent) + "%")
            return ret


    @staticmethod
    def get_red_candle_not_alarmed():
        alerts = []
        conn = sqlite3.connect(get_path_db())
        cur = conn.cursor()
        alarmed = 0
        param = (alarmed,)
        sql = 'select * from red_candle where alarmed = ? limit 20'

        for row in cur.execute(sql, param):
            alerts.append(row)

        conn.close()
        return alerts

    def __validate_between_old_red_candle(self):
        return True