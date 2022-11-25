import time

import MetaTrader5 as mt5

mt5.initialize()


# Resgata o último preço negociado de um ativo
stock = "PETR4"
sel = mt5.symbol_select(stock, True)

select_stock = mt5.symbol_info(stock)._asdict()

while True:
    time.sleep(5)
    print(mt5.symbol_info_tick(stock).last)

mt5.shutdown()
