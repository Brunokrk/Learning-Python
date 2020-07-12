def open_arq(arq):
    return(open(arq, 'r'))
    
def label (matriz, line, column, rot):
    """Rotula a posição passada"""
    matriz[line][column] = rot

def checking_neighbors(matriz, pilha, line, column, rot):
    """Checa a vizinhança do nodo"""
    if (line < matriz.lines and matriz[line][column + 1] == 1):
        #direita
        column = column + 1
        pilha.push(line, column)
        print(len(pilha))
        label(matriz, line, column, rot)
    elif(line < matriz.columns and matriz[line + 1][column] == 1):
        #abaixo
        line = line + 1
        pilha.push(line, column)
        print(len(pilha))
        label(matriz, line, column, rot)
    elif (matriz.columns!=0 and matriz[line][column - 1] == 1):
        #esquerda
        column = column -1
        pilha.push(line, column)
        print(len(pilha))
        label(matriz, line, column, rot)
    elif (matriz.lines != 0 and matriz[line - 1][column] == 1):
        #acima
        line = line - 1
        pilha.push(line, column)
        print(len(pilha))
        label(matriz, line, column, rot)
    else:
        #Não existem mais vizinhos
        pilha.pop()
        print(len(pilha))

