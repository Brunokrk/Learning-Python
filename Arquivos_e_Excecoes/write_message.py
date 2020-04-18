filename='Arquivos_e_Excecoes/message.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("i love creating apps that can run ina a browser.\n")
# w -> escrita
# r -> leitura
# a -> concatenação
# r+ -> leitura e escrita
