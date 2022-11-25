import MetaTrader5 as mt5

mt5.initialize()


# Resgata informações de um ativo
ticker = "PETR4"
sel = mt5.symbol_select(ticker, True)

select_stock = mt5.symbol_info(ticker)._asdict()

for prop in select_stock:
    print("{} = {}".format(prop, select_stock[prop]))

mt5.shutdown()

