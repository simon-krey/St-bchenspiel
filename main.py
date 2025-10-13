import random as r

choices = ["rock", "paper", "scissors"]

run = True
while run:
    cc = r.choice(choices)

    uc = input("Please enter you're choice: ")
    if uc.lower() in choices:
        pass

    else:
        print("please choose one of these options: ")
