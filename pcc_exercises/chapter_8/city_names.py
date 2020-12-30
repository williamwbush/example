def city_country(city, country):
    print(city.title() + ", " + country.title())

while True:
    print("\nEnter the name of a city.")
    print("To quit, type 'q'.")
    city = input("")
    if city.lower() == 'q':
        break
    country = input("Enter the corresponding country: ")
    if country.lower() == 'q':
        break
    city_country(city, country)  
