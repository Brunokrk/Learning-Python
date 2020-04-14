class User():
    """Modelar um usuário"""
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.full_name = first_name +" "+last_name
        self.login_attempts = 0

    def describe_user(self):
        print("Name: "+ self.full_name.title())
        print("Age: "+ str(self.age))
        print("Location: "+self.location.title())

    def greet_user(self):
        print("\nBem vindo á plataforma, "+ self.full_name.title()+"!")
    
    def increment_login_attempts(self):
        """Adiciona uma tentativa """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reseta as tentativas"""
        self.login_attempts = 0
        print("Tentativas resetadas")
    
    def get_login_attempts(self):
        return self.login_attempts

user_A = User('Bruno','Pires',19,'Joinville')

user_A.greet_user()
user_A.describe_user()
user_A.increment_login_attempts()   
user_A.increment_login_attempts()   
user_A.increment_login_attempts()   
user_A.increment_login_attempts()   
user_A.increment_login_attempts()  
user_A.increment_login_attempts() 
print(str(user_A.get_login_attempts())+" tentativas de login")
user_A.reset_login_attempts()
print(str(user_A.get_login_attempts())+" tentativas de login")


