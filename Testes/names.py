from name_function import get_formated_name

print("Enter Q at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        print("---- FIM DA EXECUÇÃO----")
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        print("---- FIM DA EXECUÇÃO----")
        break

    formatted_name = get_formated_name(first, last)
    print("\t Neatly formatted_name: "+formatted_name + '.')

