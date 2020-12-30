# Dictionary of cities and their info.
cities = {
    'chicago': {
        'country': 'united states',
        'population': 2000000,
        'predominant language': 'english',
        },
    'paris': {
        'country': 'paris',
        'population': 2000000,
        'predominant language': 'french',
        },
    'tokyo': {
        'country': 'japan',
        'population': 9000000,
        'predominant language': 'japanese',
        }
    }
# Prints info on every city.
for city, city_info in cities.items():
    print("\nHere are some facts about " + city.title() + ":")
    print("\t" + "Country: " + city_info['country'].title())
    print("\t" + "Population: " + str(city_info['population']))
    print("\t" + "Predominant Language: " + 
        city_info['predominant language'].title() + "\n")
    