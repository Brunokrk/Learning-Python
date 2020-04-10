#aqui ficará as funções utilizadas no código
def make_pizza(size,*toppings):
    """Apresenta a pizza que estamos preparando"""
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
        