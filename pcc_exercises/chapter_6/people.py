people = []
person_1 = {
    "first_name": "Julia", 
    "last_name": "Bush", 
    "age": 31, 
    "city": "St. Louis",
    }
people.append(person_1)
person_2 = {
    "first_name": "Louise", 
    "last_name": "Bush", 
    "age": 32, 
    "city": "Evanston",
    }
people.append(person_2)
person_3 = {
    "first_name": "Marc", 
    "last_name": "Bush", 
    "age": 70, 
    "city": "St. Louis",
    }
people.append(person_3)
for person in people:
    print("\nFirst Name: " + person['first_name'].title())
    print('Last Name: ' + person['last_name'].title())
    print('Age: ' + str(person['age']).title())
    print('City: ' + person['city'].title() + "\n")
