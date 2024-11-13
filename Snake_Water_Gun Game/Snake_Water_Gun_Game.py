import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (type 's' for snake, 'w' for water and 'g' for gun): ")
youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}
reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}
you = youDict[youstr]

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")


# Main Logic
if(computer == you):
    with open("Result.txt", "w") as Result:
        Result.write("It's a draw!")
    
else:
    if((computer - you) == -1 or (computer - you) == 2):
        with open("Result.txt", "w") as Result:
            Result.write("Computer Wins, You Lose!!")
        
    else:
        with open("Result.txt", "w") as Result:
            Result.write("Computer Loses, You Win!!")
