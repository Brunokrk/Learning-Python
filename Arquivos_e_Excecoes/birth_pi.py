with open('Arquivos_e_Excecoes/pi_digits.txt') as file_object:
    lines = file_object.readlines() #metodo readlines() armazena cada linha em uma lista

pi_string='' #armazena os dígitos de pi
for line in lines:
    pi_string += line.strip() #adiciona cada uma das linhas (removendo a quebra de linha no final) á pi_string


birthday = input('Enter your birthday: ')
if birthday in pi_string:
    print("Your birthday appears in pi number")
else:
    print("Your birthday does not appears in pi number")


