#
# Criando lista e printando
#
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 0 primeiro item da lista, -1 último item da lista
print(bicycles[0].title())
print(bicycles[-1].title())


#
# Alterando, Adicionando e Removendo itens
#
bicycles[0] = 'Hup Naja'    # alterando primeiro elemento
print(bicycles[0].title())

bicycles.append('trek')  # add item
print(bicycles)

bicycles.insert(0, 'caloi')  # insere na posição desejada
print(bicycles)

del bicycles[0]  # deleta em posição específica
print(bicycles)


# remove o ultimo elemento (ou um específico, adicionando o indice como parâmetro da função pop) e permite trabalhar com o mesmo
popped_bicycles = bicycles.pop()
print(bicycles)
print(popped_bicycles)

# remove item conhecendo apenas o seu valor (Apenas a primeira ocorrência)
bicycles.remove('cannondale')
print(bicycles)


#
# Organização de listas
#
bicycles.sort()  # ordem alfabética
print(bicycles)
bicycles.sort(reverse=True)  # ordem alfabética inversa
print(bicycles)

# printa em ordem alfabética, mas não altera as posições de fato
print(sorted(bicycles))

bicycles.reverse()  # inverte a lista
print(bicycles)

tam = len(bicycles)  # descobre tamanho da lista
print(tam)
