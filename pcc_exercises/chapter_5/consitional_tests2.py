shoes = 'slippers'
print('Are you wearing boots?')
print(shoes == 'boots')
piano = 'kawai'
print('Is that a kawai piano?')
print(piano == 'Kawai'.lower())
print('Are you at least 21?')
print(31 >= 21)
print('Are you under 12 years old?')
print(31 < 12)
print('Are you over 17 years old?')
print(31 > 17)
print('Are you 31 or younger?')
print(31 <= 31)
print('Are you American and at least 18 years old?')
print('American' == 'american'.title() and 31 >= 18)
print('Can you build Chichen Itza?')
resources = ['oil']
gold = 8
print(('oil' in resources and gold >= 8) or gold >= 10)
print('Can you build Chichen Itza?')
resources = []
gold = 9
if 'oil' not in resources and gold < 10:
    print('You need oil or more gold to build Chichen Itza')
