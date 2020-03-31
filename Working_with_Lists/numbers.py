for value in range(1, 5):  # começa a contar em 1 e termina em 5
    print(value)

numbers = list(range(1, 6))  # list converte o conjunto de numeros em uma lista
print(numbers)

# terceiro parâmetro é a constante de contagem
even_numbers = list(range(2, 11, 2))
print(even_numbers)


# funçoes que procuram valores específicos
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


squares = [value**2 for value in range(1, 11)]
print(squares)
