import random

user_wins = 0

computer_wins = 0

options = ["rock","paper","scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input=='q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(1,3)
    # rock:1, paper:2 , scissors : 3

    computer_pick = options[random_number-1]
    print(computer_pick,"computer picked")

    if user_input=='rock' and computer_pick=='scissors':
        print("you won")
        user_wins+=1
    elif user_input=='scissors' and computer_pick=='paper':
        user_wins+=1
        print('you won')
    elif user_input=='paper' and computer_pick =="rock":
        user_wins+=1
        print('you won')
    else:
        computer_wins+=1
        print("computer won")

print("you won",user_wins,"times and computer wins",computer_wins, "times")


