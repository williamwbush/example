sandwich_orders = [
    'cuban',
    'pastrami',
    'blt',
    'pastrami',
    'pastrami',
    'brie',
    'ham',
    ]
print('\nThe deli has run out of pastrami.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('\nYour ' + sandwich + ' sandwich has been made.')
    finished_sandwiches.append(sandwich)
print('\nThese are the sandwiches that have been made')
for sandwich in finished_sandwiches:
    print('\t' + sandwich.title())
 
