# Verifica a simetria da matriz
def verifica_simetria(matriz, ordem):
    for i in range(ordem):
        for j in range(ordem):
            if not (matriz[i][j] == matriz[j][i]):
                return False
    return True

# Programa principal
def main():
    # Leitura dos dados
    ordem = int(input())
    matriz = []
    for i in range(ordem):
        linha_lida = input()
        linha_string = linha_lida.split(' ')
        linha_numeral = []
        for valor in linha_string:
            linha_numeral.append(float(valor))
        matriz.append(linha_numeral)
    
    # Verifica a simetria
    if verifica_simetria(matriz, ordem):
        print('MATRIZ SIMETRICA')
    else:
        print('MATRIZ ASSIMETRICA')

main()