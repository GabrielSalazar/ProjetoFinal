import time

from bus.update_data import main_update_data


def prepare_update_func():
    main_update_data()


def prepare_find_ticker_signals():
    main_find_ticker_signals()


def create_principal_menu():
    clear_screen()
    print("----------------------")
    print("MENU")
    print("----------------------")
    print("1 - ATUALIZAÇÃO DE ATIVOS")
    print("2 - BUSCA DE SINAIS")
    print("----------------------")
    option = input("Digite a opção desejada:\n")

    if option.isdigit():
        if int(option) == 1:
            prepare_update_func()
        elif int(option) == 2:
            prepare_find_ticker_signals()
        elif int(option) == 9:
            create_principal_menu()
        else:
            selected_option_error(create_principal_menu)
    else:
        selected_option_error(create_principal_menu)


def clear_screen():
    lines = 100
    print("\n" * lines)

    '''
    try:
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)
    '''


def selected_option_error(func):
    print("Opção inválida, tente novamente")
    time.sleep(2)
    func()