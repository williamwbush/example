my_pizzas = ["margherita", "garbage", "detroit", "sausage", "supreme"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("hawaiian")
friend_pizzas.append("cheese")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
