'''
    Entrada:
        Dia mês e ano na mesma linha, separados por um espaçamento
    Saída:
        DJ e 𝛿, em graus e com até duas casas decimais
'''
import math

# Retorna True ou False se o ano eh bissexto
def ano_bissexto(ano):
    # Se divisivel por 400, o ano eh bissexto
    if (ano % 400 == 0):
        return True
    # Se nao divisivel por 100, o ano eh bissexto
    elif (ano % 100 == 0):
        return False
    # Se divisivel por 4, o ano eh bissexto
    elif (ano % 4 == 0):
        return True
    # Caso contrario, o ano nao eh bissexto
    else:
        return False

# Calcula o dia juliano
def dia_juliano(dia, mes, ano):
    numero_dias = dia
    contador_mes = 1
    while contador_mes < mes:
        if contador_mes in (1, 3, 5, 7, 8, 10, 12):
            numero_dias += 31
        elif contador_mes in (4, 6, 9, 11):
            numero_dias += 30
        else:
            if ano_bissexto(ano):
                numero_dias += 29
            else:
                numero_dias += 28
        contador_mes += 1
    return numero_dias

# Calcula o angulo da declinacao solar
def calcula_declinacao_solar(dia, mes, ano):
    return 23.45 * math.sin(math.radians(360 / 365 * (284 + dia_juliano(dia, mes, ano))))

# Programa principal
def main():
    dados = input().split()
    dia = int(dados[0])
    mes = int(dados[1])
    ano = int(dados[2])

    print('DJ = {}'.format(dia_juliano(dia, mes, ano)))
    print('𝛿 = {:.2f}º'.format(calcula_declinacao_solar(dia, mes, ano)))

main()
    
