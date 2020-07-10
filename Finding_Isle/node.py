class Node():
    """Modelagem de cada nodo da pilha"""
    def __init__(self, line, column):
        """Construtor do nodo"""
        self.line = line
        self.column = column
        self.next = None
        