def open_arq():
    """Abre arquivo em modo leitura"""
    arq = open("Finding_Isle/map_in.txt",'r')
    return(arq)

def label (matriz, line, column, rot):
    """Rotula a posição passada"""
    matriz[line][column] = rot

def checking_neighbors(matriz, pilha, line, column, rot):
    """Checa a vizinhança do nodo"""
    if (matriz[line][column + 1] == 1):
        #direita
        pilha.push(line, column)
        label(matriz, line, column, rot)
    elif(matriz[line + 1][column] == 1):
        #abaixo
        pilha.push(line, column)
        label(matriz, line, column, rot)
    elif (matriz[line][column - 1] == 1):
        #esquerda
        pilha.push(line, column)
        label(matriz, line, column, rot)
    elif (matriz[line - 1][column] == 1):
        #acima
        pilha.push(line, column)
        label(matriz, line, column, rot)
    else:
        #Não existem mais vizinhos
        pilha.pop()

