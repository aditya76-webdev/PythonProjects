# learning:- This simple project is to master if else and elif conditions in python and also to become more comfortable
# with how to take input in python

# Descriptioin:- what you have to do in this project is to take name of user as input now you have to cross the journey or something
# so at each point you have to make decision like to move left or right
# when user decide something then on the basis of that you have to take new decisions this will help you to use if elif and else conditions
# more clearly

name = input("Type your name ")
print("Welcome",name,"to this adventure!")

answer = input("You are on a dirt road ,it has come to an end and you can go left and right. which way would you like to go? ")
answer = answer.lower()
if answer.lower()=='left':
    answer = input("You come to a river , you can walk around it or you can swim to swim across! Type walk to walk around or type swim to swim ")
    if answer.lower()=='swim':
        print("You swam across and were eaten by alligator")
    elif answer.lower()=='walk':
        print("You walked for many miles, ran out of  water and you lost the game")
    else:
        print("Not a valid option. You lose.")

elif answer.lower()=='right':
    answer = input("You come to a bridge! It looks wobbly , do you want to cross it or head it to back (cross/back)")
    if answer.lower() == 'back':
        print("You go back to the main road. Now you can decide to drive to the left or go to right ")
    elif answer.lower() == 'cross':
        answer = input("You cross the bridge and meet a stranger do you talk to them ")
        if answer.lower()=='yes':
            print("you talk to the stranger and they will give you gold and eventually you win")
        elif answer.lower()=='no':
            print('you ignored the stranger now they got offended due to which you lost')
    else:
        print("Not a valid option. You lose.")
    print()
else:
    print('not a valid option. You lose.')

print('Thank you',name," for Playing this game!")
