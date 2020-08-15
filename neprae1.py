def main():
    # Variaveis
    elementos = ['CARBONO', 'NIQUEL', 'NIQUEL E CROMO', 'MOLIBDENIO', 'CROMO', 'CROMO E VANADIO', 'CROMO E TUNGSTENIO', 'NIQUEL, CROMO E MOLIBDENIO' 'SILICIO E MANGANES']
    porcentagens_carbono = {}
    
    # Leitura de dados
    entrada = input()
    ligas = entrada.split(' ')
    
    # Logica do programa
    for liga in ligas:
        # Imprime 'ERRO' se o numero que representa a liga tiver menos que 4 caracteres
        if not(len(liga) == 4):
            print('ERRO')
        else:
            # Converte as strings lidas para numerais
            elemento = int(liga[0])
            porcentagem_elemento = float(liga[1])
            porcentagem_carbono = (10 * float(liga[2]) + float(liga[3]))/100
            
            # Calcula o percentual dos elementos
            if elemento == 1:
                porcentagem_elemento += porcentagem_carbono
                porcentagens_carbono[liga] = porcentagem_elemento
            else:
                porcentagens_carbono[liga] = porcentagem_carbono
            
            # Imprime o nome do elemento adicionado e sua respectiva porcentagem
            print(porcentagem_elemento, elementos[elemento-1])
    
    # Imprime a liga com mais carbono percentualmente
    print(max(porcentagens_carbono, key=porcentagens_carbono.get))

main()