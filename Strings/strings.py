name = "bruno marchi pires"
print(name.title())
print(name.upper())
print(name.lower())


first_name = "Bruno"
middle_name = "Marchi"
last_name = "Pires"
full_name = first_name + " " + middle_name + " " + last_name
print(full_name)

#   \t -> tabulação
#   \n -> quebra de linha

first_name = "           Bruno           "

print(first_name.rstrip())  # remove espaços no lado direito
print(first_name.lstrip())  # remove espaços no lado esquerdo
print(first_name.strip())  # remove espaços em ambos os lados

age = 19
message = "Happy "+str(age)+"rd Birthday"  # transforma int em caracter
print(message)
