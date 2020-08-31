# Leitura dos dados
def leitura_dados():
    ## Quantidade de bases (inercial e moveis) que o sistema mecânico é composto
    quantidade_bases = int(input())
    ## Vetor que se deseja realizar a transicao para outra base
    vetor = input().split()
    ## Base correspondente ao vetor e a base que se deseja transferir o vetor (na mesma linha)
    bases = input().split()
    ## Matrizes de transformacao de coordenadas de uma base para outra (sempre da anterior para posterior)
    ordem_matrizes = 3
    matrizes = []
    for i in range(quantidade_bases - 1):
        matriz = []
        for j in range(ordem_matrizes):
            linha = input().split()
            matriz.append(linha)
        matrizes.append(matriz)
    # Dicionario que retorna com os dados
    dados = {}
    dados['quantidade_bases'] = quantidade_bases
    dados['vetor'] = vetor
    dados['bases'] = bases
    dados['matrizes'] = matrizes
    return dados

# Retorna a matriz transposta
def matriz_transposta(matriz):
    # Cria a matriz
    matriz_resultante = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append('')
        matriz_resultante.append(linha)
    
    # Calcula a matriz transposta
    for i in range(3):
        for j in range(3):
            matriz_resultante[i][j] = matriz[j][i]
    
    # Retorna a matriz transposta
    return matriz_resultante

# Retorna o resultado da multiplicacao de uma matriz por um vetor
def multiplicacao_vetorial(matriz, vetor):
    # Cria o vetor que sera retornando
    vetor_resultante = []
    for i in range(3):
        vetor_resultante.append('')
    
    # Algoritmo de multiplicacao de matriz por um vetor
    for i in range(len(matriz)):
        vetor_resultante[i] = ''
        for j in range(len(matriz[i])):
            #resultado = soma_strings(resultado, multiplica_strings(matriz[i][j], vetor[j]))
            vetor_resultante[i] = soma_strings(vetor_resultante[i], multiplica_strings(matriz[i][j], vetor[j]))
    
    # Retorna o vetor
    return vetor_resultante

# Converte as bases para numeros inteiros
def converte_bases(dados):
    base0 = dados['bases'][0]
    base1 = dados['bases'][1]

    if len(base0) == 1:
        base0 = 0
    else:
        base0 = int(base0[1])
    
    if len(base1) == 1:
        base1 = 0
    else:
        base1 = int(base1[1])
    
    # Retorna as bases em forma de tupla
    return (base0, base1)

# Imprime um vetor
def imprime_vetor(vetor):
    retorno = ''
    for j in range(3):
        print(vetor[j])

# Multiplicacao das strings
def multiplica_strings(string1, string2):
    if string1 == '0' or string2 == '0':
        return ''
    elif string1 == '1' or string2 == '1':
        if string1 == '1':
            return string2
        else:
            return string1
    else:
        if len(string1) == 0 and len(string2) == 0:
            return ''
        if len(string1) == 0:
            return string2
        if len(string2) == 0:
            return string1
        sinal = ''
        if string1[0] == '-' and string2[0] == '-':
            string1 = string1[1:]
            string2 = string2[1:]
        else:
            if string1[0] == '-':
                sinal = '-'
                string1 = string1[1:]
            if string2[0] == '-':
                sinal = '-'
                string2 = string2[1:]
        
        return (sinal + string1 + string2)

# Soma strings
def soma_strings(string1, string2):
    if len(string1) == 0 and len(string2) == 0:
        return ''
    if len(string1) == 0:
        return string2
    if len(string2) == 0:
        return string1
    sinal = '+'
    if len(string2) > 0:
        if string2[0] == '-':
            sinal = '-'
    return (string1 + sinal + string2)

def multiplica_matrizes(matriz1, matriz2):
    # Cria a matriz
    matriz_resultante = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append('')
        matriz_resultante.append(linha)
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matriz_resultante[i][j] = soma_strings(matriz_resultante[i][j], multiplica_strings(matriz1[i][k], matriz2[k][j]))

    return matriz_resultante

# Logica do programa
def main():
    dados = leitura_dados()
    (base0, base1) = converte_bases(dados)
    if base0 < base1:
        matrizes = dados['matrizes'][base0]
        for i in range(base0 - 1, base1):
            matrizes = multiplica_matrizes(matrizes, dados['matrizes'][i-1])
        vetor = multiplicacao_vetorial(matrizes, dados['vetor'])
    else:
        matrizes = matriz_transposta(dados['matrizes'][base0])
        for i in range(base1 - 1, base0):
            matrizes = multiplica_matrizes(matrizes, matriz_transposta(dados['matrizes'][i-1]))
        vetor = multiplicacao_vetorial(matrizes, dados['vetor'])
        vetor = multiplicacao_vetorial(matriz_transposta(dados['matrizes'][base0-1]), dados['vetor'])
    imprime_vetor(vetor)

main()