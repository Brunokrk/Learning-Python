import json

def greet_user():
    """Saúda o usuário pelo nome"""
    username = get_stored_username()
    if username:
        print("Welcome back, "+username+"!")
    else:
        get_new_username()
        

def get_stored_username():
    """Obtem o nome do usuário, se ja armazenado"""
    filename = 'Arquivos_e_Excecoes/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Coleta o username ainda não salvo"""
    filename = 'Arquivos_e_Excecoes/username.json'
    username = input("What's your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember u when u come back, " + username + "!")




greet_user()





