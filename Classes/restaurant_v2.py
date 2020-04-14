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

restaurant = Restaurant("habbib's", "Comida árabe")

restaurant.open_restaurant()
restaurant.set_number_served(13)
restaurant.increment_number_served(10)
