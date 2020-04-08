def greet_user (names):
    """Exibe uma saudação simples a cada usuário da lsita"""
    for name in names:
        print("Hello, "+name.title()+"!")


usernames=['hannah', 'ty', 'margot']
greet_user(usernames)