import json

filename = 'Arquivos_e_Excecoes/username.json'

with open(filename)as f_obj:
    username = json.load(f_obj)
    print("Welcome back, "+username+"!")