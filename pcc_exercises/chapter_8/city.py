def describe_city(city, country="India"):
    """Print a city and its country."""
    print(city.title() + " is in " + country + ".")

describe_city("Bangalore")
describe_city("Buenos Aires", "Argentina")
describe_city("Chennai")