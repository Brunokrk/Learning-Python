people_confirmed = {
    'jen': 'python',
    'sarah':'C',
    'edward': 'ruby',
    'phill' : 'python',
}
list_people = {
    'jen': 'python',
    'Bruno':'C',
    'sarah':'C',
    'Andrei':'C',
    'edward': 'ruby',
    'Robert': 'Html',
    'phill' : 'python',
}

for name,language in list_people.items():
    if name in people_confirmed:
        print('Parabéns, você respondeu á pesquisa\n')
    else:
        people_confirmed[name] = language

print(people_confirmed)
        