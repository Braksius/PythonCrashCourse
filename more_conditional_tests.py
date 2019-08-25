car = 'bmw'
number_1 = 20
number_2 = 10

if car == 'bmw':
    print("True")

if car != 'bmw':
    print("True")

if car.lower() == 'bmw':
    print("True")

if number_1 != number_2:
    print("True")

if number_1 >= number_2:
    print("True")

if (number_1 >= number_2) or (number_1 != number_2):
    print(number_1 == number_2)

cars = ['bmw', 'subaru', 'vw', 'toyota']

if ('subaru' in cars) or ('porshe' not in cars):
    print("True")
