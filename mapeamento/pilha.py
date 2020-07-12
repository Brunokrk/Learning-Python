from node import Node

class Pilha():
    """Modelagem de uma pilha"""
    def __init__(self):
        self.top = None
        self.size = 0
    
    def __len__(self):
        """Retorna o tamanho da pilha"""
        return self.size
    
    def __repr__ (self):
        """Retorna uma representação da pilha"""
        t=""
        ptr = self.top
        while(ptr):
            t = t + str(ptr.line)+ "," + str(ptr.column) + "\n"
            ptr = ptr.next
        return t

    def push(self, line, column):
        """Insere um elemento na pilha"""
        new_node = Node(line, column)
        
        new_node.next = self.top
        self.top = new_node
        self.size = self.size + 1
    
    def pop(self):
        """Remove o ultimo elemento da pilha"""
        if self.size > 0:
            node = self.top
            self.top = self.top.next
            self.size = self.size - 1
            return node
        raise IndexError("Empty Stack")

    def peek(self):
        """Retorna o quem está no topo da pilha"""
        if self.top == None:
            return None
        else: 
            return str(self.top.line) + str(self.top.column)

