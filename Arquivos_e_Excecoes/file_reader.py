#with open('Arquivos_e_Excecoes/pi_digits.txt') as file_object:
    # read armazena todo o conteudo do arquivo em uma longa string
#    contents = file_object.read()
#    print(contents.rstrip())

#Analisando cada linha separadamente
with open('Arquivos_e_Excecoes/pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

