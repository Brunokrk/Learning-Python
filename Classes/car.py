class Car():
    """Modelagem simples de um carro"""
    def __init__(self, make, model, year):
        """Incializa os atributos que descrevem um carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante"""
        long_name = str(self.year)+ ' '+self.make + ' '+self.model
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print("This car has "+ str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        """
        Define o valor de leitura do hodômetro com o valor especificado
        Rejeita a alterção se for tentativa de definir um valor menor para o hodometro
        """
        

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Incrementa o valor existente no odometro"""
        self.odometer_reading += miles


my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())


#Podemos modificar o valor do odometro acessando o atributo diretamente:
#my_new_car.odemeter_reading = 23
 
#Também podemos modificar utilizando um método
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('Subaru','outback',2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()