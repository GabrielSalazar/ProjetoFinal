import datetime

from bus.indicators import mom
from common.util import validate_crossover_progress, validate_crossover_return
from dice.alert import Alert


def validate_mom(data_mom, ticker, timeframe):
    alert = None
    data = mom(data_mom)

    data_sell = data.copy()
    data_buy = data.copy()


#mom  inferior_band  superior_band
    data_sell.drop(["inferior_band"], axis=1, inplace=True)
    data_sell = data_sell.rename(columns={'mom': 'curta', 'superior_band': 'longa'}, inplace=False)
    result = validate_crossover_return(data_sell)

    if result[0]:
        if result[1] == "SELL":
            #Operação é a contrária no MOM, sinalizando exaustão do movimento
            alert = Alert(datetime.datetime.today(), ticker, "", "MOM", "BUY", timeframe)

    if alert is None:
        data_buy.drop(["superior_band"], axis=1, inplace=True)
        data_buy = data_buy.rename(columns={'mom': 'curta', 'inferior_band': 'longa'}, inplace=False)
        #print(data_buy)
        result = validate_crossover_return(data_buy)

        if result[0]:
            if result[1] == "BUY":
                # Operação é a contrária no MOM, sinalizando exaustão do movimento
                alert = Alert(datetime.datetime.today(), ticker, "", "MOM", "SELL", timeframe)

    return alert;