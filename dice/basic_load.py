import datetime

from dice.ticker import Ticker
#import MetaTrader5 as mt5

global tickers_long_and_short_corr #Pares de ativos a serem acompanhados com correlação Long and Short
global ticker_with_options_follow #Ativos com opções a serem acompanhados
global ticker_follow #Ativos a serem acompanhados
global call_series #Series, letras vs meses das opções de compra
global schedule #Tempos para validação dos indicadores

def get_mini_ind():
    #Fazer lógica utilizando:
    #https://www.b3.com.br/pt_br/solucoes/plataformas/puma-trading-system/para-participantes-e-traders/calendario-de-negociacao/vencimentos/calendario-de-vencimentos-de-contratos-financeiros/
    print(str(datetime.datetime.today()))
    day = str(datetime.datetime.today())[8:10]
    year = str(datetime.datetime.today())[2:4]
    month_aux = str(datetime.datetime.today())[5:7]

    if month_aux == "01" or month_aux == "02":
        month = "G"
    elif month_aux == "03" or month_aux == "04":
        month = "J"
    elif month_aux == "05" or month_aux == "06":
        month = "M"
    elif month_aux == "07" or month_aux == "08":
        month = "Q"
    elif month_aux == "09" or month_aux == "10":
        month = "V"
    elif month_aux == "11" or month_aux == "12":
        month = "Z"

    #return "WIN" + month + year
    return "WINJ22"


def get_mini_dol():
    year = str(datetime.datetime.today())[2:4]
    month_aux = str(datetime.datetime.today())[5:7]

    if month_aux == "01":
        month = "F"
    elif month_aux == "02":
        month = "G"
    elif month_aux == "03":
        month = "H"
    elif month_aux == "04":
        month = "J"
    elif month_aux == "05":
        month = "K"
    elif month_aux == "06":
        month = "M"
    elif month_aux == "07":
        month = "N"
    elif month_aux == "08":
        month = "Q"
    elif month_aux == "09":
        month = "U"
    elif month_aux == "10":
        month = "V"
    elif month_aux == "11":
        month = "X"
    elif month_aux == "12":
        month = "Z"

    return "WDO" + month + year

schedule = []

not_schedule = [
        {"time": "10:09"},
        {"time": "10:10"},
        {"time": "11:04"},
        {"time": "11:05"},
        {"time": "12:04"},
        {"time": "12:05"},
        {"time": "13:04"},
        {"time": "13:05"},
        {"time": "14:04"},
        {"time": "14:05"},
        {"time": "15:04"},
        {"time": "15:05"},
        {"time": "16:04"},
        {"time": "16:05"},
        {"time": "17:04"},
        {"time": "17:05"},
        {"time": "18:14"},
        {"time": "18:15"}
]

#adicionar no not_schedule
schedule_break_up = []

schedule_break_up = [
        {"time": "10:30"},
        {"time": "11:00"},
        {"time": "11:30"},
        {"time": "12:00"},
        {"time": "12:30"},
        {"time": "13:00"},
        {"time": "13:30"},
        {"time": "14:00"},
        {"time": "14:30"},
        {"time": "15:00"},
        {"time": "15:30"},
        {"time": "16:00"},
        {"time": "16:30"},
        {"time": "17:00"},
        {"time": "17:30"},
        {"time": "18:00"},
        {"time": "18:20"},
]

call_series = [
    {"month":"01",
     "serie": "A",
     "exerciseDay": ""
     },
    {"month": "02",
     "serie": "B",
     "exerciseDay": ""
     },
    {"month": "03",
     "serie": "C",
     "exerciseDay": ""
     },
    {"month": "04",
     "serie": "D",
     "exerciseDay": ""
     },
    {"month": "05",
     "serie": "E",
     "exerciseDay": ""
     },
    {"month": "06",
     "serie": "F",
     "exerciseDay": ""
     },
    {"month": "07",
     "serie": "G",
     "exerciseDay": ""
     },
    {"month": "08",
     "serie": "H",
     "exerciseDay": ""
     },
    {"month": "09",
     "serie": "I",
     "exerciseDay": "17"
     },
    {"month": "10",
     "serie": "J",
     "exerciseDay": "15"
     },
    {"month": "11",
     "serie": "K",
     "exerciseDay": "19"
     },
    {"month": "12",
     "serie": "L",
     "exerciseDay": "17"
     }
]


ticker_follow = [
    {"ticker":	"ABCB4"},
    {"ticker":	"ABEV3"},
    {"ticker":	"AESB3"},
    {"ticker":	"AGRO3"},
    {"ticker":	"ALUP11"},
    {"ticker":	"ARZZ3"},
    {"ticker":	"ASAI3"},
    {"ticker":	"AZUL4"},
    {"ticker":	"B3SA3"},
    {"ticker":	"BBAS3"},
    {"ticker":	"BBDC3"},
    {"ticker":	"BBDC4"},
    {"ticker":	"BBSE3"},
    {"ticker":	"BEEF3"},
    {"ticker":	"BIDI11"},
    {"ticker":	"BMGB4"},
    {"ticker":	"BPAC11"},
    {"ticker":	"BPAN4"},
    {"ticker":	"BRAP4"},
    {"ticker":	"BRDT3"},
    {"ticker":	"BRFS3"},
    {"ticker":	"BRKM5"},
    {"ticker":	"BRML3"},
    {"ticker":	"BRSR6"},
    {"ticker":	"BTOW3"},
    {"ticker":	"CAML3"},
    {"ticker":	"CASH3"},
    {"ticker":	"CCRO3"},
    {"ticker":	"CEAB3"},
    {"ticker":	"CESP6"},
    {"ticker":	"CIEL3"},
    {"ticker":	"CMIG4"},
    {"ticker":	"COGN3"},
    {"ticker":	"CPFE3"},
    {"ticker":	"CPLE6"},
    {"ticker":	"CRFB3"},
    {"ticker":	"CSAN3"},
    {"ticker":	"CSMG3"},
    {"ticker":	"CSNA3"},
    {"ticker":	"CVCB3"},
    {"ticker":	"CYRE3"},
    {"ticker":	"DIRR3"},
    {"ticker":	"DTEX3"},
    {"ticker":	"ECOR3"},
    {"ticker":	"EGIE3"},
    {"ticker":	"ELET3"},
    {"ticker":	"ELET6"},
    {"ticker":	"EMBR3"},
    {"ticker":	"ENAT3"},
    {"ticker":	"ENBR3"},
    {"ticker":	"ENEV3"},
    {"ticker":	"ENGI11"},
    {"ticker":	"EQTL3"},
    {"ticker":	"EZTC3"},
    {"ticker":	"FESA4"},
    {"ticker":	"FLRY3"},
    {"ticker":	"GFSA3"},
    {"ticker":	"GGBR4"},
    {"ticker":	"GNDI3"},
    {"ticker":	"GOAU4"},
    {"ticker":	"GOLL4"},
    {"ticker":	"GRND3"},
    {"ticker":	"GUAR3"},
    {"ticker":	"HAPV3"},
    {"ticker":	"HGTX3"},
    {"ticker":	"HYPE3"},
    {"ticker":	"IGTA3"},
    {"ticker":	"IRBR3"},
    {"ticker":	"ITSA4"},
    {"ticker":	"ITUB4"},
    {"ticker":	"JBSS3"},
    {"ticker":	"JHSF3"},
    {"ticker":	"JPSA3"},
    {"ticker":	"KLBN11"},
    {"ticker":	"LAME4"},
    {"ticker":	"LCAM3"},
    {"ticker":	"LEVE3"},
    {"ticker":	"LJQQ3"},
    {"ticker":	"LOGG3"},
    {"ticker":	"LPSB3"},
    {"ticker":	"LREN3"},
    {"ticker":	"LWSA3"},
    {"ticker":	"MDIA3"},
    {"ticker":	"MEAL3"},
    {"ticker":	"MGLU3"},
    {"ticker":	"MILS3"},
    {"ticker":	"MOVI3"},
    {"ticker":	"MRFG3"},
    {"ticker":	"MRVE3"},
    {"ticker":	"MULT3"},
    {"ticker":	"NGRD3"},
    {"ticker":	"NTCO3"},
    {"ticker":	"ODPV3"},
    {"ticker":	"PCAR3"},
    {"ticker":	"PETR3"},
    {"ticker":	"PETR4"},
    {"ticker":	"PETZ3"},
    {"ticker":	"PNVL3"},
    {"ticker":	"POMO4"},
    {"ticker":	"POSI3"},
    {"ticker":	"PRIO3"},
    {"ticker":	"PTBL3"},
    {"ticker":	"QUAL3"},
    {"ticker":	"RADL3"},
    {"ticker":	"RAIL3"},
    {"ticker":	"RAPT4"},
    {"ticker":	"RENT3"},
    {"ticker":	"RRRP3"},
    {"ticker":	"SANB11"},
    {"ticker":	"SAPR11"},
    {"ticker":	"SAPR4"},
    {"ticker":	"SBSP3"},
    {"ticker":	"SEER3"},
    {"ticker":	"SEQL3"},
    {"ticker":	"SLCE3"},
    {"ticker":	"SQIA3"},
    {"ticker":	"STBP3"},
    {"ticker":	"SULA11"},
    {"ticker":	"SUZB3"},
    {"ticker":	"TAEE11"},
    {"ticker":	"TASA4"},
    {"ticker":	"TCSA3"},
    {"ticker":	"TEND3"},
    {"ticker":	"TIMS3"},
    {"ticker":	"TOTS3"},
    {"ticker":	"TUPY3"},
    {"ticker":	"UGPA3"},
    {"ticker":	"UNIP6"},
    {"ticker":	"USIM5"},
    {"ticker":	"VALE3"},
    {"ticker":	"VIVA3"},
    {"ticker":	"VIVT3"},
    {"ticker":	"VLID3"},
    {"ticker":	"VULC3"},
    {"ticker":	"VVAR3"},
    {"ticker":	"WEGE3"},
    {"ticker":	"WIZS3"},
    {"ticker":	"YDUQ3"}
]

''''
ticker_with_options_follow = [
    #{'ticker': '^BVSP'},
    {'ticker':	'ABEV3'},
    {'ticker':	'AZUL4'},
    {'ticker':	'B3SA3'},
    {'ticker':	'BBAS3'},
    {'ticker':	'BBDC4'},
    {'ticker':  'BOVA11'},
    {'ticker':  'BRFS3'},
    {'ticker':	'COGN3'},
    {'ticker':	'CSNA3'},
    {'ticker':	'ELET6'},
    {'ticker':	'GGBR4'},
    {'ticker':	'GOAU4'},
    {'ticker':	'IRBR3'},
    {'ticker':  'ITUB4'},
    {'ticker':	'JBSS3'},
    {'ticker':	'MGLU3'},
    {'ticker':	'MRFG3'},
    {'ticker':	'PETR4'},
    {'ticker':	'SUZB3'},
    {'ticker':	'USIM5'},
    {'ticker':	'VALE3'},
    {'ticker':	'VIIA3'},
    {'ticker':	'WEGE3'}
]
'''

ticker_with_options_follow = [
    #{'ticker': '^BVSP'},
    #{'ticker': '^SPX'},
    #{'ticker': '^IXIC'},
    #{'ticker': '^DJI'},
    #{'ticker': 'GC=F'},
    #{'ticker': 'CL=F'},

    #{'ticker': 'PBR'},
    #{'ticker': 'VALE'},
    #{'ticker': 'ITUB'},
    #{'ticker': 'BBD'},


    {'ticker':	'B3SA3'},
    {'ticker':	'BBAS3'},
    {'ticker':	'BBDC4'},
    {'ticker':	'CSNA3'},
    {'ticker':	'ELET6'},
    {'ticker':	'GGBR4'},
    {'ticker':	'GOAU4'},
    {'ticker':  'ITUB4'},
    {'ticker':	'MGLU3'},
    {'ticker':	'MRFG3'},
    {'ticker':	'PETR4'},
    {'ticker':	'SUZB3'},
    {'ticker':	'USIM5'},
    {'ticker':	'VALE3'},
    {'ticker':	'WEGE3'}
]


tickers_long_and_short_corr = [
     {"long": "GGBR4",
     "short": "USIM5"},

    {"long": "GGBR4",
     "short": "GOAU4"},

    {"long": "CSNA3",
     "short": "USIM5"},

    {"long": "ITUB4",
     "short": "ITSA4"},

    {"long": "ITUB4",
     "short": "BBDC4"},

    {"long": "ITUB4",
     "short": "BBAS3"},

    {"long": "BBAS3",
     "short": "BBSE3"},

    {"long": "BRSR6",
    "short": "ITUB4"},

    {"long": "AZUL4",
    "short": "GOLL4"},

    {"long": "SANB11",
    "short": "BRSR6"},

    {"long": "VALE3",
    "short": "USIM5"}
]

'''
def add_new_ticker():
    with_negotiation = []
    without_negotiation = []
    mt5.initialize()
    tickers = mt5.symbols_get()


    for ticker in tickers:
        tk = Ticker(ticker.name)
        if len(ticker.name) <= 6 and validate_ticker_stock(ticker.name):
            if tk.with_options() and get_deals_ticker(ticker.name):
                with_negotiation.append(ticker.name)
            else:
                without_negotiation.append(ticker.name)
        else:
            without_negotiation.append(ticker.name)

        tk = None

    print("Com negócios")
    print("")
    for with_neg in with_negotiation:
        print(with_neg)

    print(len(with_negotiation))
    print("")
    print("")

    # print("Sem negócios")
    # print("")
    # for without_neg in without_negotiation:
    #     print(without_neg)
    # print(len(without_negotiation))
    mt5.shutdown()

def get_deals_ticker(ticker):
    sel = mt5.symbol_select(ticker, True)
    select_ticker = mt5.symbol_info(ticker)._asdict()
    if int(select_ticker["session_deals"]) > 100:
        return True
    else:
        return False
'''

def validate_ticker_stock(ticker):
    tamanho = len(ticker)
    final_com_dois = ticker[(tamanho-2):tamanho]
    final_com_um = ticker[-1]
    if len(ticker) == 5:
        if final_com_um == "3" or final_com_um == "4" or final_com_um == "6" or final_com_um == "5" and not final_com_dois.isnumeric():
            return True
        else:
            return False
    else:
        if final_com_dois == "11":
            return True
        else:
            return False

'''
def is_fii(ticker):
    sel = mt5.symbol_select(ticker, True)
    select_ticker = mt5.symbol_info(ticker)._asdict()
    if select_ticker["description"].find("FII") > 0:
        return True
    else:
        return False
'''



#add_new_ticker()

# ticker = Ticker("PETR4", "ON", "PETROBRAS", "PETRÓLEO", "S", "S", "N")
#
# ticker.ticker = "CSNA3"
# print(ticker.ticker)



# db = Dbase()
# query_result =  db.execute_query("SELECT * FROM finance_data.stocks")
# print(str(len(query_result)))
#
# for x in query_result:
#     print(x)
