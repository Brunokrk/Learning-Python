def car_information (fabricante, modelo, **car_info):
    """Constrói um dicionário com tudo que sabemos sobre o carro"""
    settings={}
    settings['fabricante_carro']=fabricante
    settings['modelo_carro']=modelo

    for key,value in car_info.items():
        settings[key]=value

    return settings

car = car_information('volvo','A3',iadjsji='hauuahs',ahfuhu='pasfk')
print(car)