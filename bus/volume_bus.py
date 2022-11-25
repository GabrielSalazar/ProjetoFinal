import math
import time
from bus.indicators import volume_plus_3, ifr
from dice.alert import Alert
from dice.red_candle import RedCandle


def get_ifr_df(data):
    ifr_list = []
    for i in range(0, len(data)):
        ifr_list.append(data.iloc[i]['IFR14'])

    #print(len(ifr_list))
    return ifr_list


def get_operation(p_variation_volume, p_ifr):

    oper = "NONE"
    try:
        if 150 <= p_variation_volume < 200:
            if p_ifr >= 70:
                oper = "SELL"
        elif 200 <= p_variation_volume < 300:
            if p_ifr >= 65:
                oper = "SELL"
        elif  p_variation_volume >= 300:
            if p_ifr >= 60:
                oper = "SELL"

        if oper == "NONE":
            if 150 <= p_variation_volume < 200:
                if p_ifr <= 30:
                    oper = "BUY"
            elif 200 <= p_variation_volume < 300:
                if p_ifr <= 35:
                    oper = "BUY"
            elif  p_variation_volume >= 300:
                if p_ifr <= 40:
                    oper = "BUY"

    except Exception as e:
            print('Erro ao definir operação')
            print(e)
            oper = "NONE"
    finally:
        return oper


def validate_volume(data, ticker, timeframe):
    alert = None
    i_list = []
    data_valid = volume_plus_3(data)
    #data_stoch = stoch(data)
    #data_valid['stoch'] = data_stoch['stoch']

    new_data_valid = data_valid.copy()
    i_list = get_ifr_df(ifr(data_valid))

    new_data_valid['IFR14'] = i_list



    if len(new_data_valid) > 0:
        new_data_valid = new_data_valid.tail(2)
        new_data_valid = new_data_valid.head(1)

        high = new_data_valid.iat[0,1]
        low = new_data_valid.iat[0,2]
        volume = str(new_data_valid.iat[0,5])
        variation = new_data_valid.iat[0,7]
        if math.isnan(variation):
            variation = 0
        dt = new_data_valid.index[len(new_data_valid) - 1]
        #stoch_value = data_valid.iat[0,8]
        ifr_value = new_data_valid.iat[0, 8]
        print('Volume: ' + str(volume))
        print('Variação % de entrada de volume: ' + str(round(variation,0)) + '%')
        print('IFR 14: ' + str(round(ifr_value, 0)))
        time.sleep(1)
        ''''
        Estocástico
        if stoch_value <= 28:
            oper = "BUY"
        elif stoch_value >= 76:
            oper = "SELL"
        else:
            oper = "NONE"
        '''

        if int(variation) >= 150:
            oper = get_operation(int(variation), int(ifr_value))
        else:
            oper = "NONE"

        #oper = "BUY"
        #variation = 100

        if oper != "NONE":
            if int(variation) >= 150:
                #print(data_valid)
                alert = Alert(dt, ticker, "", "VOLUME", str(oper + ' - ' + 'IFR14: ' + str(round(ifr_value, 0)) + ' - VOLUME VARIATION: ' + str(round(variation,0)) + '%'), str(timeframe))

                if alert.insert() is None:
                    alert = None
                else:
                    red_candle = RedCandle(dt, ticker, str(volume), round(variation,0) , low, high, round(ifr_value, 0), oper, timeframe, 0)
                    #Insere candle vermelho
                    if red_candle.insert() is None:
                        alert = None
                    else:
                        print(alert)
                        print(red_candle)
    return alert



#Recebe do red_candle por parâmetro
#Pesquisar IFR do red_candle
#Calcular +1% da máxima e -1% da mínima do red_candle
#Validar se preço atual ultrapassou limite de -1% da mínima ou +1% da máxima do red_candle
def validate_red_candle():
    pass
