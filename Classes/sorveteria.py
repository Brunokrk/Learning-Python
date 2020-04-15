#Exercício página 241
class Restaurant():
    """Uma tentativa de modelar um restaurante"""
    def __init__(self, restaurant_name, food_type):
        self.restaurant_name = restaurant_name
        self.food_type = food_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Descreve o restaurante"""
        print("Nome:\t"+self.restaurant_name.title() +".")
        print("Especialidade:\t"+self.food_type.title() +".")
    
    def open_restaurant(self):
        """Informa que o restaurente abriu"""
        print("O restaurante está aberto!")
    
    def set_number_served(self, number):
        """Seta o numero de atendimentos"""
        self.number_served = number
        print("O restaurante atendeu "+str(self.number_served)+" pessoas!")
    
    def increment_number_served(self, add):
        """Incrementa numero de atendimentos"""
        self.number_served += add
        print("Foram adicionados mais "+ str(add)+" atendimentos á contagem, totalizando "+str(self.number_served))

class Sorveteria(Restaurant):
    def __init__(self, restaurant_name, food_type):
        super().__init__(restaurant_name,food_type)
        self.flavors = ['chocolate','menta','abacaxi','morango','nutella']
    
    def flavors_list (self):
        for flavor in self.flavors:
            print(flavor.title())

IceCreamStand = Sorveteria('IceLand','sorvetes')
IceCreamStand.flavors_list()
