sum = 0

while True:
    number = input("Digite um numero, ou 'q' para sair: ")
    if number =='q':
        print("-----Fim da execução-----")
        break
    else:
        try:
            number = int(number)
        except ValueError:
            print("Voce não informou um número válido")
        else:
            sum += number
            print("Soma atual: "+ str(sum))