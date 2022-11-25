import MetaTrader5 as mt5

mt5.initialize()

# Busca de tickers conforme a busca. No caso veio todos ativos que contenham PETR
petr_tickers = mt5.symbols_get("*PETRG*")

for petr_ticker in petr_tickers:
    print(petr_ticker.name)

print(len(petr_tickers))

# Desconecta do MetaTrader
mt5.shutdown()