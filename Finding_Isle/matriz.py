import isle_functions 
class  Matriz():
    """Modelagem de uma Matriz"""

    def __init__(self):
        """Inicializa os atributos que descrevem uma Matriz"""
        arquivo = isle_functions.open_arq()
        self.matriz = arquivo.readlines()
        self.lines = len(self.matriz)
        self.columns = len(self.matriz[0]) - 1
        self.elements = (self.lines * self.columns)
        arquivo.close()
        
    def print_matriz(self):
        
        for line in range(self.lines):
            for column in range(self.columns):
                print(self.matriz[line][column], end='')
            print()
            

