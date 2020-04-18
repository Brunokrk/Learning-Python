filename='Arquivos_e_Excecoes/guest.txt'

name = input("Qual seu nome? ")
with open(filename,'w') as file_object:
    file_object.write(name.title())