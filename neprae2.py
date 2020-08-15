# Verifica o estado do corpo
def get_estado(temperatura_de_fusao, temperatura_final, temperatura_de_ebulicao):
    if temperatura_final <= temperatura_de_fusao:
        return 'Sólido'
    elif temperatura_final <= temperatura_de_ebulicao:
        return 'Líquido'
    else:
        return 'Gasoso'

# Calcula a temperatura final
'''
    corpo[0] = calor especifico
    corpo[1] = massa
    corpo[2] = temperatura inicial
'''
def get_temperatura_final(corpos):
    somatorio_numerador = 0
    somatorio_denominador = 0
    for corpo in corpos:
        somatorio_numerador = somatorio_numerador + corpo[1] * corpo[0] * corpo[2]
        somatorio_denominador = somatorio_denominador + corpo[1] * corpo[0]
    return somatorio_numerador / somatorio_denominador

def main():
    # Leitura dos dados
    numero_corpos = int(input())
    corpos=[]
    for i in range(numero_corpos):
        entrada = input()
        valores = entrada.split(' ')

        # Converte a leitura em string para numerais
        calor_especifico = float(valores[0])
        massa = float(valores[1])
        temperatura_inicial = float(valores[2])
        temperatura_de_fusao = float(valores[3])
        temperatura_de_ebulicao = float(valores[4])

        # Adiciona os dados convertidos para a lista
        corpo = [calor_especifico, massa, temperatura_inicial, temperatura_de_fusao, temperatura_de_ebulicao]
        corpos.append(corpo)
    
    # Calculo da temperatura final
    temperatura_final = get_temperatura_final(corpos)

    # Se tiver menos do que 2 corpos, imprime 'ERRO'
    if numero_corpos < 2:
        print('ERRO')
    else:
        # Imprime a temperatura final dos corpos
        print('{:.2f}'.format(temperatura_final))

        # Verifica o estado fisico de cada corpo
        for i in range(numero_corpos):
            print(get_estado(corpos[i][3], temperatura_final, corpos[i][4]))

main()