import isle_functions as fnc
from pilha import Pilha


class Matriz():
    """Modelagem de uma Matriz"""

    def __init__(self):
        """Inicializa os atributos que descrevem uma Matriz"""
        arquivo = fnc.open_arq("entrada.txt")
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
        rot = 2
        flag = 0
        for line in range(0, self.lines):
            print("a")
            for column in range(0, self.columns):
                print("b")
                while(flag == 0):
                    print("c")
                    if self.matriz[line][column] == 1:
                        pilha.push(line, column)
                        print(len(pilha))
                        fnc.label(self.matriz, line, column, rot)
                        fnc.checking_neighbors(
                            self.matriz, pilha, line, column, rot)
                        if(pilha.top == None):
                            rot = rot + 1
                    elif((self.matriz[line][column] == rot) and (pilha.top != None)):
                        line = pilha.top.line
                        column = pilha.top.column
                        fnc.checking_neighbors(
                            self.matriz, pilha, line, column, rot)
                        if(pilha.top == None):
                            rot = rot + 1 
                    elif(pilha.top == None):
                        flag = 1
                flag = 0
