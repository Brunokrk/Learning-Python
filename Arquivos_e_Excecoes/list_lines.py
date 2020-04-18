#criando uma lista de linhas para fechar o arquivo, e mesmo assim ter seu conteúdo 
#devidamente armazenado
with open('Arquivos_e_Excecoes/pi_digits.txt') as file_object:
    lines = file_object.readlines() #metodo readlines() armazena cada linha em uma lista

for line in lines:
    print(line.rstrip())