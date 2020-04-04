alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("Voce ganhou " + str(new_points) + " pontos")

#adicionando novas chaves
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#modificando valor de uma chave
alien_0['color'] = 'yellow'
print("O alienígena agora é " + alien_0['color'])

#excluindo uma chave
del alien_0['points']
print(alien_0)

#outra forma de definir um dicionário
favorite_lang = {
    'jen': 'python',
    'sarah':'C',
    'edward': 'ruby',
    'phill' : 'python',
}