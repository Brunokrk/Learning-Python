import isle_functions as fnc
from pilha import Pilha


class Matriz():
    """Modelagem de uma Matriz"""

    def __init__(self):
        """Inicializa os atributos que descrevem uma Matriz"""
        arquivo = open('Finding_Isle/map_in.txt', 'r')
        self.matriz = arquivo.readlines()
        self.lines = len(self.matriz)
        self.columns = len(self.matriz[0]) - 1
        self.elements = (self.lines * self.columns)
        arquivo.close()

    def print_matriz(self):
        """Printa a Matriz na tela"""
        for line in range(0, self.lines):
            for column in range(0, self.columns):
                print(self.matriz[line][column], end='')
            print()

    def finding_isles(self):
        """Método que identifica as ilhas"""
        pilha = Pilha()
        print(len(pilha))
        rot = 2
        for line in range(0, self.lines):
            for column in range(0, self.columns):
                while(1):
                    if (self.matriz[line][column] == 1):
                        pilha.push(line, column)
                        fnc.label(self.matriz, line, column, rot)
                        fnc.checking_neighbors(self.matriz, pilha, line, column, rot)
                        print(len(pilha))
                        if(len(pilha) == 0):
                            rot = rot + 1
                    elif ((self.matriz[line][column] == rot) and (len(pilha) == 0)):
                        line = pilha.top.line
                        column = pilha.top.column
                        fnc.checking_neighbors(
                            self.matriz, pilha, line, column, rot)
                        if(len(pilha) == 0):
                            rot = rot + 1
                    elif (len(pilha) == 0):
                        break
        print(pilha)


matriz = Matriz()
matriz.finding_isles()
matriz.print_matriz()
