menu = {"pizza" : 3.00,
        "nachos" : 4.50,
        "pho" : 3.60,
        "hamburger" : 3.70,
        "bread" : 2.00,
        "tea" : 1.60,
        "lemonade" : 1.50}
cart = []
total = 0

print("---------MENU---------")

for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")


print("----------------------")

while True:
    food = input("Select an item (q to quit) : ")
    if food == 'q' or food == 'Q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("The total amount you buy is :", end = " ")
for food in cart:
    total += menu.get(food)


print(total)