with open('Arquivos_e_Excecoes/pi_digits.txt') as file_object:
    lines = file_object.readlines() #metodo readlines() armazena cada linha em uma lista

pi_string='' #armazena os dígitos de pi
for line in lines:
    pi_string += line.strip() #adiciona cada uma das linhas (removendo a quebra de linha no final) á pi_string

print(pi_string[:20]+" ...")
print(len(pi_string))