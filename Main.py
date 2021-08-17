import random
import math

l = ["R","P","S"]
rounds = int(input("Enter Number Of Rounds: "))
wins = math.ceil(rounds/2)
compScore = 0
userScore = 0

while compScore != wins and userScore != wins:
    user = input("Enter Your Choice(R = Rock, P = Paper, S = Scissors) : ").upper()
    comp = random.choice(l)
    if (comp == 'R' and user == 'R') or (comp == 'S' and user == 'S') or (comp == 'S' and user == 'S'):
        print("This Round Is A Draw")
        print("Scores : ")
        print("User's Score : {}".format(userScore))
        print("Computer's Score : {}".format(compScore))
        
    elif (comp == 'R' and user == 'p') or (comp == 'P' and user == 'S') or (comp == 'S' and user == 'R'):
        print("User Wins This Round")
        userScore += 1
        print("Scores : ")
        print("User's Score : {}".format(userScore))
        print("Computer's Score : {}".format(compScore))
        
    elif (comp == 'R' and user == 'S') or (comp == 'P' and user == 'R') or (comp == 'S' and user == 'P'):
        print("Computer Wins This Round")
        compScore += 1
        print("Scores : ")
        print("User's Score : {}".format(userScore))
        print("Computer's Score : {}".format(compScore))
        
    else:
        print("Invalid Choice")
        break

print("----------------------------------------------------------------")
print("User Score =  %d" % userScore)
print("Computer Score = %d" % compScore)
if userScore > compScore:
    print("User Wins")
else:
    print("Computer Wins")