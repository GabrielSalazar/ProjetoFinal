from bus.indicators import mma
from common.util import validate_crossover_return
from dice.alert import Alert
import datetime

def validate_mma(data_mma, ticker, timeframe):
    alert = None
    data = mma(data_mma)

    data.drop(["Adj Close", "mma50"], axis=1, inplace=True)

    data = data.rename(columns = {'mma9': 'curta', 'mma21': 'longa'}, inplace = False)
    result = validate_crossover_return(data)

    if result[0] == True:
        alert = Alert(datetime.datetime.today(),ticker, "","MMA 9 21", result[1], timeframe)
        if alert.insert() is None:
            alert = None

    return alert











