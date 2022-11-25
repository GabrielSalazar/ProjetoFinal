import datetime
import time

from bus.candle_bus import validate_candle
from bus.ifr_bus import validate_ifr
from bus.indicators import ifr
from bus.mma_bus import validate_mma
from bus.volume_bus import validate_volume, validate_red_candle

from common.util import validate_schedule_time
from dice.alert import Alert
from dice.basic_load import ticker_with_options_follow, get_mini_ind

# 1 - Valida horário (Horário atual comparando com global schedule)
# 2 - Buscar ticker (global ticker_follow)
# 3 - Indicador bus (Submeter o ticker aos indicadores)
# 4 - No indicador bus get dados 1d e 60 min
# 5 - Validar dados e resultado de sinal no indicador bus
# 6 - Adicionar alerta no BD se sinal encontrado
# 7 - Enviar alerta Telegram
from dice.get_data import get_data_ticker_y

def send_alert(alert):
    msg = "\n"
    msg = msg + "----------------------- \n" + "TICKER: " + alert.ticker1 + "\n"
    msg = msg + "DATA: " + str(alert.current_date) + "\n"
    msg = msg + "INDICATOR: " + str(alert.indicator) + " - " + "OPERATION: " + str(
        alert.operation) + " - " + "TIME FRAME: " + str(alert.time_frame) + "\n"
    msg = msg + "- \n"
    msg = msg + "----------------------- \n"
    msg = msg + "\n"
    print(msg)
    Alert.simple_send(msg)


def find_ticker_signals(timeframe, find_response):
    alert_ifr = None
    alert_volume = None
    alert_candle = None
    alert_mma = None
    alert_list = []

    ticker_mini = [get_mini_ind()]

    #ticker_mini.append(get_mini_dol())

    date = datetime.datetime.today()
    start = datetime.datetime(int(str(date)[0:4]), int(str(date)[5:7]), int(str(date)[8:10]), 9, 15, 1, 125000)
    end = datetime.datetime(int(str(date)[0:4]), int(str(date)[5:7]), int(str(date)[8:10]), 17, 30, 1, 125000)

    if start <= date <= end and find_response != 'Signal' and find_response != 'Break Up':
        print("-----------------------------")
        print("")
        print("INÍCIO DA VALIDAÇÃ0 " + str(timeframe) + " min: " + str(datetime.datetime.today()))
        for mini in ticker_mini:
            print("---------------------------------------------------------------------------------------------------")
            print("Ticker: " + mini)
            data_volume = get_data_ticker_y(mini, timeframe)
            alert_volume = validate_volume(data_volume, mini, timeframe)
            if alert_volume is not None:
                print("Volume 1m encontrado. Buscando IFR 15m")
                data_ifr_15 = get_data_ticker_y(mini, "15")
                df_15 = ifr(data_ifr_15)
                df_15 = df_15.tail(1)

                ifr_value_15 = int(round(df_15.iat[0, 0], 0))

                if alert_volume.operation.split(' ')[0]  == "BUY" and ifr_value_15 <= 35:
                    send_alert(alert_volume)
                elif alert_volume.operation.split(' ')[0] == "SELL" and ifr_value_15 >= 55:
                    send_alert(alert_volume)
        print("---------------------------------------------------------------------------------------------------")
        print("FIM DA VALIDAÇÃO " + str(timeframe) + " min: " + str(datetime.datetime.today()))

    #Não é daytrade
    if timeframe != "1":
        for t in ticker_with_options_follow:  # substituir por ticker_follow
            print("")
            print("---------------------------------------------------------------------------------------------------")
            data_ifr = get_data_ticker_y(t['ticker'], timeframe)

            if len(data_ifr) > 0:
                time.sleep(0.2)
                data_volume = data_ifr.copy()
                data_candle = data_ifr.copy()
                data_mma = data_ifr.copy()

                #Aqui é o timeframe recebido por parâmetro, variável timeframe
                if timeframe == "1wk":
                    print("-")
                    print("Ticker: " + t["ticker"] + " - IFR - " + "TIMEFRAME: " + timeframe)
                    alert_ifr = validate_ifr(data_ifr, t['ticker'], timeframe)


                if timeframe == "60" or timeframe == "1d" or timeframe == "1wk":
                    print("-")
                    print("Ticker: " + t["ticker"] + " - VOLUME - " + "TIMEFRAME: " + timeframe)
                    alert_volume = validate_volume(data_volume, t['ticker'], timeframe)


                if timeframe == "1d":
                    print("-")
                    print("Ticker: " + t["ticker"] + " - PAVIO - " + "TIMEFRAME: " + timeframe)
                    alert_candle = validate_candle(data_candle, t['ticker'], timeframe)


                if timeframe == "1d":
                    print("-")
                    print("Ticker: " + t["ticker"] + " - MMA - " + "TIMEFRAME: " + timeframe)
                    data_mma.dropna(inplace=True)
                    alert_mma = validate_mma(data_mma, t['ticker'], timeframe)

                if alert_ifr is not None:
                    alert_list.append(alert_ifr)

                if alert_volume is not None:
                    alert_list.append(alert_volume)

                if alert_candle is not None:
                    alert_list.append(alert_candle)

                if alert_mma is not None:
                    alert_list.append(alert_mma)

                for alert in alert_list:
                    send_alert(alert)

                alert_list = []


def find_red_candles_signals():
    validate_red_candle()


def main_find_ticker_signals():
    f_time = True

    while True:
        if f_time == True:
            find_response = 'Signal'
            f_time = False
        else:
            find_response = validate_schedule_time()

        if find_response == 'Signal':
            #time.sleep(120)
            find_ticker_signals("60", find_response)
            find_ticker_signals("1d", find_response)
            find_ticker_signals("1wk", find_response)
        #elif find_response == 'Break Up':
        #    find_red_candles_signals()
        #else:
        #    if validate_not_schedule_time_swing_trade():
        #        pass
                #find_ticker_signals("1", find_response)

        time.sleep(60)


