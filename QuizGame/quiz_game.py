print("Welcome to my computer quiz!")

playing = input("Do You Want to Play? ")
print(playing)
count =0
if playing.lower() !='yes':
    quit()

print("Okay lets start")

answer = input("What does CPU stand for ? ".lower())

if answer.lower()=="central processing unit":
    count +=1
    print("Correct!")
else:
    print("Wrong Answer! Note: Answer should be in lowercase")

answer = input("What does RAM stand for ? ")

if answer.lower()=="random access memory":
    count +=1
    print("Correct!")
else:
    print("Wrong Answer! Note: Answer should be in lowercase")


answer = input("What does ROM stand for ? ")

if answer.lower()=="read only memory":
    count+=1
    print("Correct!")
else:
    print("Wrong Answer! Note: Answer should be in lowercase")


answer = input("What does GPU stand for ? ".lower())

if answer.lower()=="graphics processing unit":
    count+=1
    print("Correct!")
else:
    print("Wrong Answer! Note: Answer should be in lowercase")

print("you got ",count, " correct answer out of 4!")

#to learn from this project is
#1). quit() function 2). how to take prompt input 3). lowercase all characters