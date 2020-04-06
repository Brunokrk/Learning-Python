responses = {}

#flag para inidicar que a enquete está ativa
polling_active = True

while polling_active:
    #pede o nome da pessoa e a resposta
    name = input("\n Qual o seu nome: ")
    response = input("Qual montanha voce gostaria de escalar um dia: ")

    #Armazena a resposta no dicionário
    responses[name] = response

    #Descobre se outra pessoa vai responder a enquete
    repeat = input("Outra pessoa irá responder a enquete? ")
    if repeat =='no':
        polling_active = False

for name,resposne in responses.items():
    print(name+" would like to climb " +response+".B")