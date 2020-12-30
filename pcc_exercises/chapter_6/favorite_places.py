favorite_places = {}
favorite_places['William'] = ['St. Louis', 'Chicago', 'Michigan']
favorite_places['Julia'] = ['St. Louis']
favorite_places['Robert'] = ['Chicago', 'New York']
for person, places in favorite_places.items():
    if len(places) == 1:
        print("\n" + person + "'s favorite place is: " + places[0])
    else:
        print("\n" + person + "'s favorite places are:")
        for place in places:
            print("\t" + place)