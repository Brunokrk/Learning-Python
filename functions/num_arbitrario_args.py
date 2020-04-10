def make_pizza(size,*toppings):
    """Exibe a lista de ingredientes pedidos"""
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)

make_pizza(12,'pepperoni')
make_pizza(16,'mushrooms', 'green peppers', 'extra cheese')
