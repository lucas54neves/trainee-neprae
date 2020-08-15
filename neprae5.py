# Monta a matriz com todos os valores inicialmente iguais a zero
def montar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

# Monta o distanciamento
def montar_distanciamento(matriz, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            # Verifica se esta na primeira linha
            if i == 0:
                # Verifica se esta na primeira coluna
                if j == 0:
                    matriz[i][j] = 1
                else:
                    # Verifica se tem pessoa ao lado
                    if matriz[i][j-1] == 1:
                        matriz[i][j] = 0
                    else:
                        matriz[i][j] = 1
            else:
                # Verifica se esta na primeira coluna
                if j == 0:
                    # Verifica o primeiro lugar da linha anterior
                    if matriz[i-1][j] == 1:
                        matriz[i][j] = 0
                    else:
                        matriz[i][j] = 1
                else:
                    # Verifica se tem pessoa ao lado
                    if matriz[i][j-1] == 1:
                        matriz[i][j] = 0
                    else:
                        matriz[i][j] = 1

# Imprime a matriz como solicitado
def imprimir_matriz(matriz, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print('%d' %matriz[i][j])
            else:
                print('%d ' %matriz[i][j], end = '')

# Verifica a quantidade de vagas
def verifica_quantidade_vagas(matriz, linhas, colunas, quantidade_inscritos):
    quantidade_de_vagas = 0
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == 1:
                quantidade_de_vagas = quantidade_de_vagas + 1
    if quantidade_de_vagas == quantidade_inscritos:
        return 'Todos já estão em seus lugares e a palestra ja pode começar!'
    elif quantidade_de_vagas > quantidade_inscritos:
        return 'Ainda temos {} vagas para assistir a nossa palestra'.format(quantidade_de_vagas - quantidade_inscritos)
    else:
        return 'A equipe NEPRaE está disponibilizando {} cadeiras para que todos assistam a palestra'.format(quantidade_inscritos - quantidade_de_vagas)

# Programa principal
def main():
    # Leitura dos dados
    linha_lida = input()
    quantidade_inscritos = int(input())
    valores = linha_lida.split(' ')
    linhas = int(valores[0])
    colunas = int(valores[1])

    # Monta a matriz
    matriz = montar_matriz(linhas, colunas)

    # Aplica o distanciamento
    montar_distanciamento(matriz, linhas, colunas)

    # Imprime a matriz
    imprimir_matriz(matriz, linhas, colunas)

    # Imprime a informacao sobre as vagas
    print(verifica_quantidade_vagas(matriz, linhas, colunas, quantidade_inscritos))

main()