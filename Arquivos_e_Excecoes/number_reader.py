import json

filename = "Arquivos_e_Excecoes/number.json"

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)