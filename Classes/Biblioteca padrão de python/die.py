from random import randint

class Die():
    """Modelando um dado"""
    def __init__(self,sides):
        self.sides = 6
        self.qtd = 10
    
    def roll_die(self, qtd):
        self.qtd+=1
        while range(1, self.qtd):
            x = randint(1, 6)
            print(str(x))

die= Die(6)
die.roll_die(10)