with open('Arquivos_e_Excecoes/pi_digits.txt') as file_object:
    contents = file_object.read()   #read armazena todo o conteudo do arquivo em uma longa string
    print(contents.rstrip()) 

