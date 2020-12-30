rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states',
    }
for river, country in rivers.items():
    print('The ' + river.title() + ' river runs through ' + 
        country.title() + '.')
print("These are the rivers in the dictionary:")
for river in rivers.keys():
    print("\t" + river.title())
print("These are the places in the list:") 
for place in rivers.values():
    print("\t" + place.title())                                                                            