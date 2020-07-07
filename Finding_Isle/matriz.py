class  Matriz():
    """Modelagem de uma Matriz"""

    def __init__(self, lines, columns):
        """Inicializa os atributos que descrevem uma Matriz"""
        self.lines = lines
        self.columns = columns
        self.elements = (lines*columns)
        self.matriz = []

    def set_matriz(self):
        """Aloca a Matriz"""
        for i in range(self.lines):
            linha = []
            
            for j in range(self.columns):
                linha.append(0)
            
            self.matriz.append(linha)

        self.matriz[1][1] = 3
    
    def print_matriz(self):
        for i in range(self.lines):
            for j in range(self.columns):
                print(self.matriz[i][j], end='')
                print()
            
    
matriz = Matriz(5,5)
matriz.set_matriz()
matriz.print_matriz()
    

    