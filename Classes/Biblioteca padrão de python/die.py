from random import randint

class Die():
    """Modelando um dado"""
    def __init__(self,sides):
        self.sides = 6
      
    
    def roll_die(self, qtd):
        qtd+=1
        for x in range(1, qtd):
            x = randint(1, 6)
            print(str(x))

die= Die(6)
die.roll_die(2)