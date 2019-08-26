requested_toppings = ['mushrooms', 'extra cheese']

for requested_topping in requested_toppings:
    if 'mushrooms' == requested_topping:
        topping = 'mushrooms'
    if 'pepperoni' == requested_topping:
        topping = 'pepperoni'
    if 'extra cheese' == requested_topping:
        topping = 'extra cheese'
    print(f"Adding {topping}.")

print("\nFinished making your pizza!")
