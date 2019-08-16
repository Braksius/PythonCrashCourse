pizzas = ['margeritta','napolitana','scampi']
friend_pizzas = pizzas[:]
pizzas.append('cheese')
friend_pizzas.append('hawai')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("--------------------------------------")
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())