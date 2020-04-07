def describe_pet (animal_type,pet_name):
    """Exibe informações sobre um animal de estimação"""
    print("\nI have a "+ animal_type)
    print("My "+animal_type+"'s name is "+pet_name.title())
    
#argumentos devem ser fornecidos na posição de seus respectivos parametros
describe_pet(animal_type='hamster', pet_name='harry') 
