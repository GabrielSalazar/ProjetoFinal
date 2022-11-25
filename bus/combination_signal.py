#Combinações
# 1 - IFR com Volume (1)
# 2 - Média com IFR (1)
# 3 - Vol Index com Volume (Não atendida)
# 4 - RSL com volume (3)
# 5 - IFR, RSL, Volume (3)

#Pelo menos dois devem ser atendidos para alertarmos
#Um é gatilho e outro confirmação
#Em D-2

#Gatilhos e Combinações
# 1 - IFR
    # Volume
    # Medias
    # RSL

# 2 - Médias
    # IFR

# 3 - RSL
    # IFR
    # Volume

# 4 Vol Index
    # IFR
import sqlite3

from common.util import get_path_db
from dice.alert import Alert


def format_msg_alerts(alerts):
    msg = ""
    for alert in alerts:
        msg = msg + "DATA: " + str(alert[0]) + "/" + str(alert[1]) + "/" + str(alert[2]) + " " + str(alert[3]) + "\n"
        msg = msg + "INDICATOR: " + str(alert[6]) + " - " + "OPERATION: " + str(
            alert[7]) + " - " + "TIME FRAME: " + str(alert[8]) + "\n"
        msg = msg + "- \n"
    return msg

def send_alerts(alert, ind1, ind2):

    alerts = get_alerts(alert, ind1, ind2)
    msg = "----------------------- \n" + "TICKER: " + alert.ticker1 + "\n" + format_msg_alerts(alerts)
    msg = msg + "----------------------- \n"
    msg = msg + "----------------------- \n"

    Alert.simple_send(msg)


def get_alerts(alert, ind1, ind2):
    alerts = []
    conn = sqlite3.connect(get_path_db())
    cur = conn.cursor()
    alarmed = 0
    param = (alert.ticker1, ind1, ind2, alarmed,)
    sql = 'select * from alert where ticker1 = ? and indicator in (?, ?) and alarmed = ? order by current_date_year desc, current_date_month desc, current_date_day desc, current_date_time desc limit 5'

    for row in cur.execute(sql, param):
        alerts.append(row)

    conn.close()
    return alerts


def search_signal(alert, indicator):
    rows = []
    has_indicator = False
    conn = sqlite3.connect(get_path_db())
    cur = conn.cursor()

    alarmed = 0
    param = (alert.current_date.day, alert.current_date.month, alert.current_date.year, alert.ticker1, indicator, alarmed,)
    # sql = 'select indicator from alert where time_frame = ? and id = (select max(id) from alert where ticker1 = ?)'

    sql = 'select * from alert where current_date_day = ? and current_date_month = ? and current_date_year = ? and ticker1 = ? and indicator = ? and alarmed = ?'

    for row in cur.execute(sql, param):
        rows.append(row)
        break

    if len(rows) > 0:
        has_indicator = True
    cur.close()

    return has_indicator


def set_alarmed_alerts_individual(alert):
    try:
        conn = sqlite3.connect(get_path_db())
        cur = conn.cursor()

        alarmed = 0
        values = (
            alert.current_date.day, alert.current_date.month, alert.current_date.year, alert.ticker1, alert.indicator, alert.operation, alert.time_frame, alarmed)
        sql = 'update alert ' \
              'set alarmed = 1 ' \
              'where current_date_day = ? ' \
              'and current_date_month = ? ' \
              'and current_date_year = ? ' \
              'and ticker1 = ? ' \
              'and indicator = ? ' \
              'and operation = ? ' \
              'and time_frame = ? ' \
              'and alarmed = ? '
        ret = cur.execute(sql, values)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def set_alarmed_alerts_combination(alert, ind1, ind2):
    try:
        conn = sqlite3.connect(get_path_db())
        cur = conn.cursor()

        alarmed = 0
        values = (
            alert.current_date.day, alert.current_date.month, alert.current_date.year, alert.ticker1, ind1, ind2, alarmed)
        sql = 'update alert ' \
              'set alarmed = 1 ' \
              'where current_date_day = ? ' \
              'and current_date_month = ? ' \
              'and current_date_year = ? ' \
              'and ticker1 = ? ' \
              'and indicator in (?, ?) ' \
              'and alarmed = ? '
        ret = cur.execute(sql, values)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def search_signal_combination(alert):
    if alert.indicator == 'VOLUME':
        if search_signal(alert, 'IFR14'):
            send_alerts(alert, 'VOLUME', 'IFR14')
            print('send_alerts(alert, VOLUME, IFR14)')
            set_alarmed_alerts_combination(alert, 'VOLUME', 'IFR14')

    elif alert.indicator == 'IFR14':
        if search_signal(alert, 'VOLUME'):
            send_alerts(alert, 'IFR14', 'VOLUME')
            print('send_alerts(alert, IFR14, VOLUME)')
            set_alarmed_alerts_combination(alert, 'VOLUME', 'IFR14')

    elif alert.indicator == 'MOM':
        if search_signal(alert, 'MOM'):
            msg =  "DATA: " + str(alert.current_date) + "\n"
            msg = msg + "INDICATOR: " + str(alert.indicator) + "\n"
            msg = msg + "TICKER: " + str(alert.ticker1) + "\n"
            msg = msg + "OPERATION: " + str(alert.operation) + "\n"
            msg = msg + "TIME FRAME: " + str(alert.time_frame) + "\n"
            Alert.simple_send(msg)
            set_alarmed_alerts_individual(alert)

    elif alert.indicator == 'RSL':
        if search_signal(alert, 'RSL'):
            msg =  "DATA: " + str(alert.current_date) + "\n"
            msg = msg + "INDICATOR: " + str(alert.indicator) + "\n"
            msg = msg + "TICKER: " + str(alert.ticker1) + "\n"
            msg = msg + "OPERATION: " + str(alert.operation) + "\n"
            msg = msg + "TIME FRAME: " + str(alert.time_frame) + "\n"
            Alert.simple_send(msg)
            set_alarmed_alerts_individual(alert)







