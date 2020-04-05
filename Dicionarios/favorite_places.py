favorite_places = {
    'Bruno':['Ibiza', 'Dubai', 'Canadá'],
    'Andrei': ['Laguna', 'Criciúma', 'Tubarão'],
    'Roberto': ['Sidney', 'Buenos Aires', 'Sincinatti'],
    'Laura':['Whashington', 'Rio de Janeiro'],
    'Carlos':['Paris', 'Las Vegas'],
}

for name,places in favorite_places.items():
    print("Nome: " +name.title())
    for place in places:
        print("\t" + place.title() )

