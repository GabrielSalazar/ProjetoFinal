import MetaTrader5 as mt5

mt5.initialize()

# Resgata todos os ativos disponíveis na conta conectada
tickers = mt5.symbols_get()
print("Total de ativos disponíveis: ", len(tickers))


print("Os cinco primeiros ativos da lista")
counter = 0
for ticker in tickers:
    counter += 1
    print("{}. {}".format(counter, ticker.name))
    if counter == 5: break

# Desconecta do MetaTrader
mt5.shutdown()
