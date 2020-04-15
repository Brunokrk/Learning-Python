#Exercício página 241
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
    
    def fill_gas_tank(self):
        """Enche o tanque de gasolina"""
        print("Tanque de gasolina cheio")

class Battery():
    """Uma tentativa de modelar uma bateria para um carro elétrico"""
    def __init__(self, battery_size = 70):
        """Inicializa os atributos da bateria"""
        self.battery_size=battery_size
    
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria"""
        print("This car has a "+str(self.battery_size)+"-kWh battery")
    
    def get_range(self):
        """Exibe uma frase sobre a distancia que o carro é capaz de percorrer com essa bateria"""
        if self.battery_size ==70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go aproximately "+str(range)
        message += " miles on a full charge."
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print("Bateria agora de 85-kWh")
        else:
            print("A bateria não precisa de upgrade")


class ElectricCar(Car):
    """Representa aspectos de um carro específicos de veículos elétricos"""
    def __init__(self, make,model,year):
        """
        Inicializa os atributos da classe-pai
        Em seguida, inicializa os atributos específicos de um carro elétrico
        """
        super().__init__(make,model,year)
        self.battery = Battery()
    
    #Sobrescrevendo um metodo da classe pai
    def fill_gas_tank(self):
        """Carros elétricos não tem tanque de gasolina"""
        print("Este carro não possui um tanque de gasolina")
    

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()