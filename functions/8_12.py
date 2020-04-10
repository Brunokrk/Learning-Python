def sanduiche (*toppings):
    """Monta o sanduiche"""
    print("\n Sanduíche composto de :")
    for toppping in toppings:
        print("\t"+toppping)


sanduiche('queijo','maionese','presunto')
sanduiche('pasta de amendoin','geleia')
sanduiche('manteiga', 'queijo', 'oregano','tomate')