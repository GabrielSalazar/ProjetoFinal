from datetime import datetime, timedelta
from dice.basic_load import schedule, not_schedule
import os

#to get the current working directory
directory = os.getcwd()
print(directory)

def get_path_db():
    dir = os.getcwd()
    aux = dir[0:1]
    if aux == "C":
        path_db = "C:/Users/salazarg/PycharmProjects/python-finance-db"
    else:
        path_db = "/Users/salazarg/PycharmProjects/python-finance-db"

    return path_db

def get_so():
    dir = os.getcwd()
    aux = dir[0:1]
    if aux == "C":
        so = "WIN"
    else:
        so = "MAC"

    return so

def get_date_minus(days):
    d = datetime.today() - timedelta(days=days)
    d = d.strftime('%Y-%m-%d')
    return d


def remove_schedule(hour):
    try:
        hour_remove = hour - 1
        schedule.remove(hour_remove)
        print("Array ajustado: ")
        print(schedule)
    except Exception as e:
        print(e)
        print("Array: ")
        print(schedule)

def validate_schedule_time():
    response = ""
    try:
        dt = str(datetime.today())[11:16]
        hour = int(str(datetime.today())[11:13])
        min = int(str(datetime.today())[14:16])

        print("-")
        print("Aguardando: " + str(dt))

        print("Horários:")
        print("Array: ")
        print(schedule)

        if 11 <= hour <= 18:
            if hour == 11 and len(schedule) == 0:
                print("Iniciando o dia")

            if min >= 15:
                if hour in schedule:
                    response = ""
                else:
                    schedule.append(hour)
                    remove_schedule(hour)
                    response = "Signal"

        if hour >= 19:
            if len(schedule) > 0:
                schedule.clear()
                print("Fim de dia")
                print("Array vazio")
                print(schedule)

        return response
    except Exception as e:
        print('Erro varrendo horários')
        print(e)
        response = ""
    finally:
        return response


def validate_not_schedule_time_swing_trade():
    response = True
    try:
        dt = str(datetime.today())[11:16]
        for s in not_schedule:
            if dt == s['time']:
                response = False
                break
        return response

    except Exception as e:
        print("Erro varrendo horários")
        print(e)
        response = ""
    finally:
        return response


def validate_crossover_return(data):

    boo_cross = False
    data_valid = data.tail(2)
    print(data.tail(2))

    state_smaller = data_valid.head(1).iat[0,0]
    state_bigger = data_valid.head(1).iat[0,1]

    print(state_smaller, state_bigger)

    oper = "BUY" if state_smaller < state_bigger else "SELL"

    new_state_smaller = data_valid.tail(1).iat[0,0]
    new_state_bigger = data_valid.tail(1).iat[0,1]

    print(new_state_smaller, new_state_bigger, str(data_valid.tail(1).index[0])[11:16])

    if oper == "SELL":
        if new_state_smaller < new_state_bigger:
            boo_cross = True
    else:
        if new_state_smaller > new_state_bigger:
            boo_cross = True
    return boo_cross, oper


def validate_crossover_progress(data):

    boo_cross = False
    data_valid = data.tail(2)
    print(data.tail(2))

    state_smaller = data_valid.head(1).iat[0,0]
    state_bigger = data_valid.head(1).iat[0,1]

    print(state_smaller, state_bigger)

    #verifica se está dentro das bandas e qual a operação
    oper = "BUY" if state_smaller > state_bigger else "SELL"

    new_state_smaller = data_valid.tail(1).iat[0,0]
    new_state_bigger = data_valid.tail(1).iat[0,1]

    print(new_state_smaller, new_state_bigger, str(data_valid.tail(1).index[0])[11:16])

    # se cruzou para fora da banda alerta ativado
    if oper == "SELL":
        if new_state_smaller > new_state_bigger:
            boo_cross = True
    else:
        if new_state_smaller < new_state_bigger:
            boo_cross = True
    return boo_cross, oper

