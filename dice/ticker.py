#import MetaTrader5 as mt5
class Ticker:


    # region data
    def __init__(self, ticker):
        self.__ticker = ticker
        self.__type_ticker = ""
        self.__company_name = ""
        self.__sector = ""
        self.__options = ""
        self.__ibov_index = ""
        self.__small_index = ""

    @property
    def ticker(self):
        return self.__ticker

    @property
    def type_ticker(self):
        return self.__type_ticker

    @property
    def company_name(self):
        return self.__company_name

    @property
    def sector(self):
        return self.__sector

    @property
    def options(self):
        return self.__options

    @property
    def ibov_index(self):
        return self.__ibov_index

    @property
    def small_index(self):
        return self.__small_index

    @ticker.setter
    def ticker(self, ticker):
        self.__ticker = ticker

    @type_ticker.setter
    def type_ticker(self, type_ticker):
        self.__type_ticker = type_ticker

    @company_name.setter
    def company_name(self, company_name):
        self.__company_name = company_name

    @sector.setter
    def sector(self, sector):
        self.__sector = sector

    @options.setter
    def options(self, options):
        self.__options = options

    @ibov_index.setter
    def ibov_index(self, ibov_index):
        self.__ibov_index = ibov_index

    @small_index.setter
    def small_index(self, small_index):
        self.__small_index = small_index

    # endregion


    # region BUS


    # region pub

'''
    def insert_bd(self):
        db = Dbase()

        script_insert = "INSERT INTO finance_data.tickers VALUES ('{}','{}', '{}', '{}', '{}', '{}','{}')".format(self.__ticker, self.__type_ticker, self.__company_name, self.__sector, self.__options, self.__ibov_index, self.__small_index);
        response =  db.create(script_insert)
        return response

'''

'''
    def with_options(self):
        if 5 <= len(self.__ticker) <= 6:
            if len(self.__ticker) == 5:
                ticker = self.__ticker[0:-1]
            else:
                ticker = self.__ticker[0:-2]

            tickers = mt5.symbols_get(ticker)
            if len(tickers) > 300:
                return True
            else:
                return False
        return False
'''
    # endregion


    # region priv


    # endregion


    # endregion

