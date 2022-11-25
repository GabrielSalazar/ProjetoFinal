import json

import MetaTrader5 as mt5
import pandas as pd

# Conecta no MetaTrader
mt5.initialize()


# Resgatar informações da conta
account_info = mt5.account_info()
account_info_json = account_info._asdict()

#account_info_json = json.dumps(account_info)

# Como imprimir um json
for prop in account_info_json:
    print("{} = {}".format(prop, account_info_json[prop]))

# Criação de DataFrame com Pandas (Grids/Tabelas)
data_frame = pd.DataFrame(list(account_info_json.items()), columns=['property', 'value'])
print(data_frame)

# Desconecta do MetaTrader
mt5.shutdown()