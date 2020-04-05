#Exercício 6.7 da página 163
#Exercício 6.8 tem resolução identica

people = []

bruno = {
    'first': 'bruno',
    'last': 'pires',
    'age':19,
    'city':'Joinville',
}
andrei = {
    'first': 'andrei',
    'last': 'villa',
    'age':19,
    'city':'laguna',
}
italo = {
    'first': 'ítalo',
    'last': 'flôr',
    'age':19,
    'city':'laguna',
}

people.append(bruno)
people.append(andrei)
people.append(italo)

for person in people:
    print("Nome : " + person['first'].title() + " " + person['last'].title())
    print("\t Idade: " + str(person['age']).title() + "\n\t Cidade: " + person['city'].title())