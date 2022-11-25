from math import sqrt, exp, log, pi
from scipy.stats import norm

# Função para calcular os valores de 21 e d2 assim como a chamada
#  de preço. Para estender a puts, pode-se apenas adicionar uma função que
# calcula o preço de venda ou combina calls e coloca em uma única
# função que recebe um argumento especificando qual tipo de contrato
# está tratando.

def d(sigma, S, K, r, t):
    d1 = 1 / (sigma * sqrt(t)) * ( log(S/K) + (r + sigma**2/2) * t)
    d2 = d1 - sigma * sqrt(t)
    return d1, d2

def call_price(sigma, S, K, r, t, d1, d2):
    C = norm.cdf(d1) * S - norm.cdf(d2) * K * exp(-r * t)
    return C


def implied_vol(option_price, strike, spot_price, theta):
    #  Parametros da opcao
    S = spot_price  # Preço do papel a vista
    K = strike  # Strike da opção
    t = theta / 365
    r = 0.0925  # Taxa de juros
    C0 = option_price  # preço da opção

    #  Exemplo usando uma ação da apple-AAPL
    # S = 194.11
    # K = 210.0
    # t = 38.0 / 365.0
    # r = 0.01
    # C0 = 1.50

    #  Tolerancias
    tol = 1e-3
    epsilon = 1

    #  Variaveis pra controlar as iterations
    count = 0
    max_iter = 1000

    #  Precisamos fornecer um valor inicial para a raiz de nossa função
    vol = 0.50

    while epsilon > tol:
        count += 1
        if count >= max_iter:
            print('Quebrando na contagem')
            break;

       # Registra o valor calculado anteriormente para montar o percentual entre iterações

        orig_vol = vol

        #  Calcula o valor do preço de call
        d1, d2 = d(vol, S, K, r, t)
        function_value = call_price(vol, S, K, r, t, d1, d2) - C0

        #  Calcule o vega, a derivada do preço em relação a volatilidade
        vega = S * norm.pdf(d1) * sqrt(t)

        #  Atualiza o valor da volatilidade
        vol = -function_value / vega + vol

        #  Verifica a variação percentual entre a iteração atual e a última
        epsilon = abs((vol - orig_vol) / orig_vol)

    #  Imprimi os resultados
    print('Sigma = ', vol)
    print('Teve', count, ' iteracoes')


implied_vol(0.32, 17.24, 17.01, 4)




