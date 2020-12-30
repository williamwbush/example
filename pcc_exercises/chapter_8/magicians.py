mag_names = ["Belinda", "Tortu", "Maximilian", "Bob"]
new_mag_names = []

def show_magicians(names):
    """Print the names of a list"""
    for name in names:
        print(name)

def make_great(names, new_names):
    """Add the phrase 'the Great' to names in a list"""
    while names:
        new_name = names.pop()
        new_name = new_name + " the Great"
        new_names.append(new_name)

make_great(mag_names[:], new_mag_names)

show_magicians(mag_names)
show_magicians(new_mag_names)

