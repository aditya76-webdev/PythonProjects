import random

top_of_range = input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range<=0:
        print("Please! type a number greater than 0 next time")
        quit()
else:
    print("Please! type a integer number next time")
    quit()

random_num = random.randint( 0, top_of_range)
# print(random_num)
guesses = 0
while True:
    user_guess = input("Hey User guess the number : ")
    guesses+=1
    if user_guess.isdigit():
        if int(user_guess)==random_num:
            print("woah! you won, you took",guesses," guesses to win this game ")
            break
        else:
            if int(user_guess)>random_num:
                print("your guess is greater than actual answer")
            else:
                print("your guess is less than actual answer")
    else:
        print("Please enter integer num and it should be greater than zero")


#1).stricting input handling 2). randomrange 3). randomint 4).quit() 5). randint 6).break keyword
#7).infinite while loop 8).diff b/w print("i m ",age , " old") and print("i m " + str(age) +" old")