class User():
    """Modelar um usuário"""
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.full_name = first_name +" "+last_name

    def describe_user(self):
        print("Name: "+ self.full_name.title())
        print("Age: "+ str(self.age))
        print("Location: "+self.location.title())

    def greet_user(self):
        print("\nBem vindo á plataforma, "+ self.full_name.title()+"!")

user_A = User('Bruno','Pires',19,'Joinville')
user_B = User('Andrei','Villa',19,'Laguna')
user_C = User('Ítalo','Flor','19','Joinville')

user_A.greet_user()
user_A.describe_user()    

user_B.greet_user()
user_B.describe_user()  

user_C.greet_user()
user_C.describe_user()  