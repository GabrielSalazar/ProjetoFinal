from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import pytz


# Delimitando tamanho do DataFrame

pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

timezone = pytz.timezone('ETC/UTC')


# Pega o dia de hoje no formato yyyy-mm-dd
today_date = datetime.today().strftime('%Y-%m-%d')

# Concatena a data de hoje com o horário 10:00:00, data de início de pregão
today_date_negotiation = today_date + '-10:00:00'

# Realiza a operação data hora atual - início do pregão
# Essa diferença é retornada entre horário atual e início do pregão para explicitar quanto tempo do dia precisamos analisar
diff_start_negociation = datetime.today() - pd.Timestamp(today_date_negotiation)

# Time frame escolhido de 5 min
time_frame_negociation = 5

# Conversão para int da diferença do horário atual e início do prgão. Assim teremos a quantidade de segundos desta faixa de horário a ser analisada
# Total de segundos dividido pelo time frame * 60
# Total segundos / (timeframe * 60)
count_candles = int(diff_start_negociation.total_seconds()/(time_frame_negociation * 60))

mt5.initialize()

stock = "PETR4"
sel = mt5.symbol_select(stock, True)

# Resgatando do ativo selecionado, pelo timerame de 5 min, todos os candles de um dia
candles = mt5.copy_rates_from(stock, mt5.TIMEFRAME_M5, datetime.today(), count_candles)

candles_frame = pd.DataFrame(candles)
#
# # Formatando o formato da hora do DataFrame
candles_frame['time'] = pd.to_datetime(candles_frame['time'], unit='s')

print(candles_frame)

mt5.shutdown()