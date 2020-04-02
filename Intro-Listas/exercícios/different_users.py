#exercício 5.10 página 137
current_users = ['Bruno', 'José', 'Arthur', 'Robson', 'Antônio']
new_users = ['Andrei', 'José', 'Carlos', 'Robson', 'Roberto']

for new_user in new_users:
    if new_user in current_users:
        print(new_user+" Não está disponível para uso")
    else:
        print(new_user+ " Está disponível para uso")
    