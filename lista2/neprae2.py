class Tabela:
    def __init__(self):
        self.dados = {}
        self.dados['preto'] = [0,0,1,-1]
        self.dados['marrom'] = [1,1,10,1]
        self.dados['vermelho'] = [2,2,100,2]
        self.dados['laranja'] = [3,3,1000,-1]
        self.dados['amarelo'] = [4,4,10000,-1]
        self.dados['verde'] = [5,5,100000,0.5]
        self.dados['azul'] = [6,6,1000000,0.25]
        self.dados['violeta'] = [7,7,10000000,0.1]
        self.dados['cinza'] = [8,8,100000000,0.05]
        self.dados['branco'] = [9,9,1000000000,-1]
        self.dados['dourado'] = [-1,-1,0.1,5]
        self.dados['prateado'] = [-1,-1,0.01,10]
    
    def calcular_resistencia(self, cores):
        if self.cores_validadas(cores):
            resistencia = (self.dados[cores[0]][0] * 10 + self.dados[cores[1]][1]) * self.dados[cores[2]][2]
            (resistencia, unidade) = self.manipular_resistencia(resistencia)
            variacao = resistencia * self.dados[cores[3]][3] / 100
            print('O valor do resistor é de {} ± {} {}Ω'.format(resistencia, variacao, unidade))
    
    def manipular_resistencia(self, resistencia):
        if resistencia < 1000:
            return (resistencia, '')
        elif 1000 <= resistencia and resistencia < 1000000:
            resistencia = resistencia / 1000
            return (resistencia, 'k')
        elif 1000000 <= resistencia and resistencia < 1000000000:
            resistencia = resistencia / 1000000
            return (resistencia, 'M')
        else:
            resistencia = resistencia / 1000000000
            return (resistencia, 'G')

    def cores_validadas(self, cores):
        # Verifica se teve quatro cores na entrada
        if not len(cores) == 4:
            print('É necessário inserir 4 cores')
            return False
        else:
            # Verifica se a cor esta na posicao correta
            cores_incorretas = []
            posicao = 0
            
            while posicao < len(cores):
                cor = cores[posicao]
                faixas = self.dados.get(cor)
                if faixas[posicao] == -1:
                    cores_incorretas.append((cor, posicao))
                posicao += 1
            
            if len(cores_incorretas) > 0:
                # Imprime a quantidade cores digitadas erradas e quais foram
                cores = ''
                for cor in cores_incorretas:
                    cores += cor[0] + ' '
                print('Você digitou {} cores incorretas: {}'.format((len(cores_incorretas)), cores))

                # Imprime a cor e em qual posicao a cor nao pode ser implementada
                for cor in cores_incorretas:
                    print('A cor {} não pode ser implementada na posição {}'.format(cor[0], cor[1]+1))
                
                # Retorna falso para a validade da entrada
                return False
            else:
                # Retorna verdadeiro para a validade da entrada
                return True

def main():
    programa = Tabela()

    # Leitura das cores
    cores = input().split()

    programa.calcular_resistencia(cores)

main()
