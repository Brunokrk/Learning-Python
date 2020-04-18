filename="Arquivos_e_Excecoes/guest_book.txt"

flag = True

while flag:
    name = input("Qual seu nome? ")
    if name == 'exit':
        flag = False
    else:
        with open(filename,'a') as file_object:
            file_object.write(name.title()+"\n")
        print("Nome adicionado á lista de convidados!")