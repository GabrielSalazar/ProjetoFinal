import os


def create_principal_menu():
    while True:
        clear_screen()

        #get_tickers_with_more_alerts()

        #get_last_alerts()

        print("----------------------")
        print("MENU PRINCIPAL")
        print("1 - Atualizar")
        print("2 - Ticker")
        print("----------------------")

        option = input("Digite a opção desejada:\n")

        if option.isdigit():
            if int(option) == 1:
                pass
            elif int(option) == 2:
                clear_screen()

                ticker = input("Escolha o ticker:\n")
                #get_last_ticker_alerts()

                while True:
                    analysis = input("Escolha a análise:\n")
                    print("----------------------")
                    print("ANÁLISE")
                    print("1 - IFR")
                    print("2 - VOLUME")
                    print("3 - D-TREND")
                    print("4 - MMA")
                    print("5 - PROPHET")
                    print("9 - Voltar")
                    print("----------------------")

                    clear_screen()
                    if int(option) == 9:
                        pass
                    else:
                        timeframe = input("Escolha o timeframe:\n")

                        if int(analysis) == 1:
                            pass
                        elif int(analysis) == 2:
                            pass
                        elif int(analysis) == 3:
                            pass
                        elif int(analysis) == 4:
                            pass
                        elif int(analysis) == 5:
                            pass
                        else:
                            pass

                    clear_screen()
                    again = input("Outra análise?:\n")
                    print("----------------------")
                    print("ANÁLISE")
                    print("1 - SIM")
                    print("2 - NÃO")

                    if int(analysis) == 1:
                        pass
                    elif int(analysis) == 2:
                        break


def clear_screen():
    lines = 100
    print("\n" * lines)

    try:
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)


create_principal_menu()