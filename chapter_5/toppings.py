requested_toppings = ['mushrooms', 'extra cheese']

for requested_topping in requested_toppings:
    if 'mushrooms' == requested_topping:
        topping = 'mushrooms'
    elif 'pepperoni' == requested_topping:
        topping = 'pepperoni'
    elif 'extra cheese' == requested_topping:
        topping = 'extra cheese'
    print(f"Adding {topping}.")

# No for loop

if 'mushrooms' in requested_toppings:
    topping = 'mushrooms'
elif 'pepperoni' in requested_toppings:
    topping = 'pepperoni'
elif 'extra cheese' in requested_toppings:
    topping = 'extra cheese'
print(f"Adding {topping}.")

print("\nFinished making your pizza!")
