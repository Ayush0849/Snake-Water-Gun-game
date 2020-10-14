import random
name = input("Please enter your name\n")
Score_of_computer = 0
Score_of_Player = 0
no_of_chances = 10
while no_of_chances > 0:
    select = input(
        "Please enter: \tS for snake\n\t W for water\n\t G for gun\n")
    computer = ["snake", "water", "gun"]
    Choice = random.choice(computer)
    print(Choice)
    if select == 'S':
        if Choice == "snake":
            print("No one got a point")
        elif Choice == "water":
            print("You got a point!")
            Score_of_Player = Score_of_Player + 1
        elif Choice == "gun":
            print("You lost a point")
            Score_of_computer = Score_of_computer + 1
    elif select == "W":
        if Choice == "water":
            print("No one got a point")
        elif Choice == "snake":
            print("You lost a point")
            Score_of_computer = Score_of_computer + 1 
        elif Choice == "gun":
            print("You got a point")
            Score_of_Player = Score_of_Player + 1
    elif select == "G":
        if Choice == "gun":
            print("No one got a point")
        if Choice == "snake":
            print("You got a point")
            Score_of_Player = Score_of_Player + 1
        if Choice == "water":
            print("You lost a point")
            Score_of_computer = Score_of_computer + 1 
    else:
        print("Input Error!")
        quit()
    no_of_chances = no_of_chances - 1
if Score_of_computer > Score_of_Player:
    print("Soory! ",name, " you have lost this game")
    print("Your score: ", Score_of_Player)
    print("Computer score: ", Score_of_computer)
else:
    print("Congratulations! ",name," you have won this game!")
    print("Your score: ", Score_of_Player)
    print("Computer score: ", Score_of_computer)
    
