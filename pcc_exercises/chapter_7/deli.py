sandwich_orders = [
    'cuban',
    'pastrami',
    'blt',
    'brie',
    'ham',
    ]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("\nI made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)
print('\nThese sandwiches have been made:')
for sandwich in finished_sandwiches:
    print(sandwich)



