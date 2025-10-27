import random

choices = ["rock",'paper',"scissor"]

userscore = 0
computerscore = 0 

for round in range (1,4):
    print(f"round:{round}")
    userchoice = str(input("rock - paper - scissor :: ' ' ").lower())
    
    if userchoice not in choices:
        print("dont go out of the box")

computerchoice = random.choice(choices)
print(f"opponent choose this {computerchoice}")

if computerchoice == userchoice:
    print("this is a tie ")
elif(
    (userchoice =="rock" and computerchoice == "scissor") or
    (userchoice == "paper" and computerchoice == "rock") or 
    (userchoice == "scissor" and computerchoice == "paper")
    
): 
    print("you win the round ")
    userscore=+1
else:
    print("computer wins")
    computerscore=+1

print("time for the final score ")
print(f"your score {userscore}  || computer score {computerscore}")

if userscore > computerscore:
    print("you win")
elif computerscore > userscore:
    print("computer wins")
else:
    print("its a draw but close ")