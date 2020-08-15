# Calculo o enesimo termo
def calcula_termo(primeiro_termo, razao, posicao_termo):
    return primeiro_termo * pow(razao, (posicao_termo - 1))

# Verifica se a serie converge
def verifica_convergencia(razao):
    if abs(razao) < 1:
        return True
    else:
        return False

# Calcula a soma infinita
def soma_infinita(primeiro_termo, razao):
    return primeiro_termo / (1 - razao)

# Calcula a soma parcial
def soma_parcial(primeiro_termo, razao, posicao_termo):
    return primeiro_termo * (pow(razao, posicao_termo) - 1) / (razao - 1)

# Programa principal
def main():
    # Leitura dos dados
    primeiro_termo = float(input())
    razao = float(input())
    posicao_termo = int(input())

    # Calcula o enesimo termo
    enesimo_termo = calcula_termo(primeiro_termo, razao, posicao_termo)
    
    # Imprime as informacoes solicitadas
    print(enesimo_termo)
    if verifica_convergencia(razao):
        print('CONVERGENTE')
        print(soma_infinita(primeiro_termo, razao))
    else:
        print('DIVERGENTE')
        print(soma_parcial(primeiro_termo, razao, posicao_termo))

main()