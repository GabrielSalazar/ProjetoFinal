import datetime

import requests
import sqlite3

from common.util import get_path_db


class Alert:

    def __init__(self, current_date, ticker1, ticker2, indicator, operation, time_frame):
        self.__current_date = current_date
        self.__ticker1 = ticker1
        self.__ticker2 = ticker2
        self.__indicator = indicator
        self.__operation = operation
        self.__time_frame = time_frame

    @property
    def current_date(self):
        return self.__current_date

    @property
    def ticker1(self):
        return self.__ticker1

    @property
    def ticker2(self):
        return self.__ticker2

    @property
    def indicator(self):
        return self.__indicator

    @property
    def operation(self):
        return self.__operation

    @property
    def time_frame(self):
        return self.__time_frame


    @current_date.setter
    def current_date(self, current_date):
        self.__current_date = current_date

    @ticker1.setter
    def ticker1(self, ticker1):
        self.__ticker1 = ticker1

    @ticker2.setter
    def ticker2(self, ticker2):
        self.__ticker2 = ticker2

    @indicator.setter
    def indicator(self, indicator):
        self.__indicator = indicator

    @operation.setter
    def operation(self, operation):
        self.__operation = operation

    @time_frame.setter
    def time_frame(self, time_frame):
        self.__time_frame = time_frame

    @staticmethod
    def simple_send(msg):
        headers = {
            'Content-Type': 'application/json',
        }

        data = '{"chat_id": "-507094150", "text": "' + msg + '", "disable_notification": false}'
        response = requests.post('https://api.telegram.org/bot1887199692:AAHs9u_tS_z1Ikzi4b6HD_-iooQcYLLC5pA/sendMessage',headers=headers, data=data)
        print(response.text)


    def insert(self):
        try:
            conn = sqlite3.connect(get_path_db())
            cur = conn.cursor()

            #Pega a janela do movimento e guarda para ser usada no insert
            window = str(self.__current_date)[11:16]

            # Quando timeframe semanal ele considera o último dia da semana.
            if self.__time_frame == "1w":
                self.current_date = datetime.datetime.today()
            values = (
            self.__current_date.day, self.__current_date.month, self.__current_date.year, window,
            self.__ticker1, self.__indicator, self.__operation, self.__time_frame)

            sql = 'insert into alert (current_date_day, ' \
                  'current_date_month, ' \
                  'current_date_year, ' \
                  'current_date_time, ' \
                  'ticker1, ' \
                  'indicator, ' \
                  'operation, ' \
                  'time_frame) values (?, ?, ?, ?, ?, ?, ?, ?)'
            ret = cur.execute(sql, values)
            conn.commit()
            conn.close()
        except Exception as e:
            print("Indicator: " + self.__indicator + " Timeframe: " + self.__time_frame + " Ticker: " + self.__ticker1 + " repetido")
            print(e)
            ret = None
        finally:
            print("-")
            print("NOVO ALERTA CADASTRADO TICKER: " + self.__ticker1 + " - INDICADOR: " + self.__indicator + " - TIMEFRAME: " + self.__time_frame)
            return ret


    def __different_alert(self):
        rows = []
        is_different = False
        conn = sqlite3.connect(get_path_db())
        cur = conn.cursor()
        param = (self.__time_frame, self.__current_date.day, self.__current_date.month, self.__current_date.year, self.__operation, self.__ticker1, self.__indicator,)


        sql = 'select * from alert ' \
              'where time_frame = ? ' \
              'and current_date_day = ? ' \
              'and current_date_month = ? ' \
              'and current_date_year = ? ' \
              'and operation = ?' \
              'and ticker1 = ?' \
              'and indicator = ?'

        for row in cur.execute(sql, param):
            rows.append(row)
            break

        if len(rows) == 0:
            is_different = True

        cur.close()

        return is_different




