def count_words (filename):
    """Conta o numero aproximado de palavras em um arquivo"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file "+filename+"does not exist.")
    else:
        #Conta o numero de palavras
        words= contents.split()
        num_words = len(words)
        print("Thes file "+filename+" has about "+str(num_words)+" words. ")

filenames=['Arquivos_e_Excecoes/alice.txt','Arquivos_e_Excecoes/pi_digits.txt','Arquivos_e_Excecoes/guest_book.txt','Arquivos_e_Excecoes/error_test.txt']

for filename in filenames:
    count_words(filename)