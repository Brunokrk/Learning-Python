class Restaurant():
    """Uma tentativa de modelar um restaurante"""
    def __init__(self, restaurant_name, food_type):
        self.restaurant_name = restaurant_name
        self.food_type = food_type
    
    def describe_restaurant(self):
        """Descreve o restaurante"""
        print("Nome:\t"+self.restaurant_name.title() +".")
        print("Especialidade:\t"+self.food_type.title() +".")
    
    def open_restaurant(self):
        """Informa que o restaurente abriu"""
        print("O restaurante está aberto!")

restaurant = Restaurant("habbib's", "Comida árabe")

restaurant.open_restaurant()
restaurant.describe_restaurant()