def make_pizza(*toppings):
    """Exibe a lista de ingredientes pedidos"""
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
