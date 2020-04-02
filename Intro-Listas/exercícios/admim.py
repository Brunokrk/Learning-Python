# exercício 5.8, 5.9, página 136

users = ['Bruno', 'José', 'Arthur', 'admin', 'Antônio']

if users:
    for user in users:
        if user == 'admin':
            print("Olá Admin, gostaria de ver um relatório de status?")
        else:
            print("Bem vindo " + user)
else:
    print("Precisamos encontrar alguns usuários")
