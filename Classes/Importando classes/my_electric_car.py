from car import Car, ElectricCar

my_tesla = ElectricCar('tesla','model s',2016)
my_beetle = Car('Volkswagen','beetle',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print(my_beetle.get_descriptive_name())

#
#Podemos importar todo o módulo e usar a notação de ponto
#
#import car
#my_beetle = car.Car('Volkswagen','beetle',2016)
#print(my_tesla.get_descriptive_name())
#


#
#Podemos também importar todas as classes de um módulo
#
#from car import *
#