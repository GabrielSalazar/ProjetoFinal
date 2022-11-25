import datetime

from bus.indicators import vol_index_detrand
from common.util import validate_crossover_return
from dice.alert import Alert


def validate_vol_index_detrand(data, ticker):
    alert = None
    data = vol_index_detrand(data)

    data_sell = data.copy()
    data_buy = data.copy()

    # Valida se cruzou O superior_band
    data_sell.drop(['mm_afastamento', 'inferior_band'], axis=1, inplace=True)
    data_sell = data_sell.rename(columns={'afastamento': 'curta', 'superior_band': 'longa'}, inplace=False)
    # print(data_sell)
    result = validate_crossover_return(data_sell)

    if result[0] == True:
        alert = Alert(datetime.datetime.today(), ticker, '', 'VOL INDEX SELL', result[1], '60')

    # Não houve cruzamento do superior_band
    # Buscar então no inferior_band
    if alert is None:
        data_buy.drop(['superior_band', 'mm_afastamento'], axis=1, inplace=True)
        # Valida se IFR cruzou 30 pra cima
        data_buy = data_buy.rename(columns={'afastamento': 'curta', 'inferior_band': 'longa'}, inplace=False)
        # print(data_buy)
        result = validate_crossover_return(data_buy)

        if result[0] == True:
            alert = Alert(datetime.datetime.today(), ticker, '', 'VOL INDEX BUY', result[1], '60')

    return alert;