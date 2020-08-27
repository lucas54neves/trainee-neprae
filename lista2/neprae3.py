class Numero:
    def __init__(self, sinal, valor):
        self.sinal = sinal
        self.valor = valor
    
    def multiplica(self, outro_numero):
        # Multiplicacao de sinal
        if self.sinal == outro_numero.sinal:
            sinal = '+'
        else:
            sinal = '-'

        # Multiplicacao por zero
        if self.valor == '0' or outro_numero.valor == '0':
            valor = ''
            sinal = ''
        # Multiplicacao por 1
        elif self.valor == '1' or outro_numero.valor == '1':
            if self.valor == '1' and not outro_numero.valor == '1':
                valor = outro_numero.valor
            elif not self.valor == '1' and outro_numero.valor == '1':
                valor = self.valor
            else:
                valor = '1'
        else:
            valor = self.valor + outro_numero.valor
        return Numero(sinal, valor)
    
    def soma(self, outro_numero):
        sinal = ''
        valor = self.valor + outro_numero.sinal + outro_numero.valor
        return Numero(sinal, valor)

class Transformacao:
    def __init__(self):
        # Leitura dos dados
        ## Quantidade de bases (inercial e moveis) que o sistema mecânico é composto
        self.quantidade_de_bases = int(input())
        ## Vetor que se deseja realizar a transicao para outra base
        self.vetor = input().split()
        ## Base correspondente ao vetor e a base que se deseja transferir o vetor (na mesma linha)
        self.bases = input().split()
        ## Matrizes de transformacao de coordenadas de uma base para outra (sempre da anterior para posterior)
        self.ordem_matrizes = 3
        self.matrizes = []
        for i in range(self.quantidade_de_bases - 1):
            matriz = []
            for j in range(self.ordem_matrizes):
                linha = input().split()
                matriz.append(linha)
            self.matrizes.append(matriz)
    
    def get_matriz_transposta(self, matriz):
        # Cria a matriz
        matriz_transposta = []
        for i in range(self.ordem_matrizes):
            linha = []
            for j in range(self.ordem_matrizes):
                linha.append(0)
            matriz_transposta.append(linha)

        # Calcula a matriz transposta
        for i in range(self.ordem_matrizes):
            for j in range(self.ordem_matrizes):
                matriz_transposta[i][j] = matriz[j][i]
        
        # Retorna a matriz transposta
        return matriz_transposta
    
    def multiplica_vetor_matriz(self, vetor, matriz):
        matriz_resultante = []
        for i in range(self.ordem_matrizes):
            linha = []
            for j in range(self.ordem_matrizes):
                linha.append(Numero('', '0'))
            matriz_resultante.append(linha)

        for i in range(self.ordem_matrizes):
            for j in range(self.ordem_matrizes):
                for k in range(self.ordem_matrizes):
                    print(vetor[i][k])
                    vet = vetor[i][k]
                    mat = matriz[k][j]
                    mult = self.converte_para_numero(vet).multiplica(self.converte_para_numero(mat))
                    matriz_resultante[i][j] = matriz_resultante[i][j].soma(mult)
        
        return matriz_resultante

    # Converte uma string em um numero (sinal e valor)
    def converte_para_numero(self, palavra):
        if palavra[0] == '-':
            return Numero('-', palavra.replace('-',''))
        else:
            return Numero('+', palavra)
    
    # Logica do programa
    def executar(self):
        base0 = self.bases[0]
        base1 = self.bases[1]

        if len(base0) == 1:
            base0 = 0
        else:
            base0 = int(base0[1])
        
        if len(base1) == 1:
            base1 = 0
        else:
            base1 = int(base1[1])

        if base0 < base1:
            matriz = self.multiplica_vetor_matriz(self.vetor[base0], self.matrizes[base1])
        else:
            matriz = self.multiplica_vetor_matriz(self.vetor[base0], self.get_matriz_transposta(self.matrizes[base1]))
        
        for i in range(self.ordem_matrizes):
            print(matriz[i])

def main():
    # Leitura dos dados
    transformacao = Transformacao()
    transformacao.executar()
    '''
    n1 = Numero('+', 'Teste')
    n2 = Numero('-', 'Testando')
    n3 = n1.multiplica(n2)
    print('{}{}'.format(n3.sinal, n3.valor))
    print(len('B1'))
    print(len('II'))
    print(len('I'))
    '''

main()