import random


low = 1
high = 100
number = random.randint(low, high)
# print(number)
# options = ("rock", "paper", "scissors")
# option = random.choice(options)
# print(option)
# cards = ["1", "2", "3", "j", "Q", "k"]
# random.shuffle(cards)
# print(cards)

guesses = 0
while True:
    guess = int(input(f"Enter a number between {low} - {high}: "))
    guesses += 1

    if guess <number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print("Exactly")