fnumbers =  {
    "Julia": [1, 89],
    "Louise": [2, 88], 
    "Mom": [3], 
    "Dad": [4], 
    "Susie": [5, 3]
    }
for name, favorite_numbers in fnumbers.items():
    if len(favorite_numbers) == 1:
        print("\n" + name + "'s favorite number is " + str(favorite_numbers[0]) + ".")
    else:
        print("\n" + name + "'s favorite numbers are:")
        for number in favorite_numbers:
            print("\t" + str(number))
