user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}
favorite_lang = {
    'jen': 'python',
    'sarah':'C',
    'edward': 'ruby',
    'phill' : 'python',
}

#percorrendo todos os pares chave-valor com um laço
for key, value in user_0.items():
    print('\n key: '+ key)
    print('Value: '+value)

for name,language in favorite_lang.items():
    print("\nName: " + name)
    print("Language: "+language)

#percorrendo todas as chaves com um laço (OBS: usar o metodo keys é opcional, visto que o comportamento nomal de um
# laço for, é percorrer somente as chaves)
for name in favorite_lang.keys():
    print(name.title())

#percorrendo todos os valores ocm um laço, aqui o uso do metodo values é necessário
for name in favorite_lang.values():
    print(name.title())