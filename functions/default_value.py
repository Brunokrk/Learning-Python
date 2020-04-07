def describe_pet (pet_name,animal_type='dog'):
    """Exibe informações sobre um animal de estimação"""
    print("\nI have a "+ animal_type)
    print("My "+animal_type+"'s name is "+pet_name.title())
    
#argumentos devem ser fornecidos na posição de seus respectivos parametros
describe_pet(pet_name='Willie') 
