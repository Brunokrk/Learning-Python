#Apenas um exemplo de como funcionam os inputs

prompt = "Mesa para quantas pessoas: "
people =input(prompt)
people = int(people)


if people > 8:
    print("Terão que esperar liberar uma mesa")
else:
    print("Sua mesa está pronta")