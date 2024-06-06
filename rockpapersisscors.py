import os, random


global CPUScore, playerScore, Rock, Sisscors, Paper
Rock = "Rock"
Sisscors = "Sisscors"
Paper = "Paper"

R = 'Rock'
P = 'Paper'
S = 'Sisscors'

CPU = (R, P, S)

playerScore = 0
CPUScore = 0

def mainMenu():
    os.system("cls")
    print("Welcome to Rock Paper Sisscors")
    print("-------------------------------")
    print("[1] Play against CPU")
    print("[2] Exit the Program")
    print("[3] Tutorial")
    print("[4] Points/Score")
    match input("Choose:\n"):
        case "1":
            PVC()
        case "2":
            exit_Area()
        case "3":
            tutorial()
        case "4":
            score_Track()
        case _:
            input("Invalid Entry")
            mainMenu()



#CODE- PLAYER AGAINST CPU -CODE
def PVC():
    os.system("cls")
    match input("Type the letter 'm' to go to main menu or 'p' to play against the CPU:\n"):
        case 'm':
            mainMenu()
        case 'p':
            CPU_Active()
        case _:
            input("Invalid Entry")
            PVC()

def CPU_Active():
    os.system("cls")
    print("Type 'm' to go to main menu\n\n")
    match input("[R] Rock\n[P] Paper\n[S] Sisscors:\n: "):    
        case "R":
            while True:
                print(f"You've selectd 'Rock'")
                if (random.choice(CPU)) == P:
                    print("Computer chose Paper")
                    global CPUScore, playerScore
                    CPUScore += 1
                    playerScore += 0
                    print(f"You lose!\nCPU Score: {CPUScore}\nPlayer Score: {playerScore}")
                    input()
                    CPU_Active()
                    return (random.choice(CPU)), CPUScore, playerScore
                if (random.choice(CPU)) == R:
                    print("Computer chose Rock")
                    CPUScore += 0
                    playerScore += 0
                    print(f"Tie!\nCPU Score: {CPUScore}\nPlayer Score: {playerScore}")
                    input()
                    CPU_Active()
                    return (random.choice(CPU)), CPUScore, playerScore
                if (random.choice(CPU)) == S:
                    print("Computer chose sisscors")
                    CPUScore += 0
                    playerScore +=1
                    print(f"You Win!\nCPU Score: {CPUScore}\nPlayer Score: {playerScore}") 
                    input()
                    CPU_Active()
                    return (random.choice(CPU)), CPUScore, playerScore

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------

        case "P":
            while True:
                print("You've selected 'Paper'")
                if (random.choice(CPU)) == P:
                    print("Computer chose Paper")
                    CPUScore += 0
                    playerScore += 0
                    print(f"You Tie!\nCPU Score: {CPUScore}\nPlayer Score: {playerScore}")
                    input()
                    CPU_Active()
                    return (random.choice(CPU)), CPUScore, playerScore
                if (random.choice(CPU)) == R:
                    print("Computer chose Rock")
                    CPUScore += 0
                    playerScore += 1
                    print(f"You Win!\nCPU Score: {CPUScore}\nPlayer Score: {playerScore}")
                    input()
                    CPU_Active()
                    return (random.choice(CPU)), CPUScore, playerScore
                if (random.choice(CPU)) == S:
                    print("Computer chose sisscors")
                    CPUScore += 1
                    playerScore += 0
                    print(f"You Lose!\nCPU Score: {CPUScore}\nPlayer Score: {playerScore}") 
                    input()
                    CPU_Active()
                    return (random.choice(CPU)), CPUScore, playerScore
        
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------


        case "S":
            while True:
                print("You've Selected 'Sisscors'")
                if (random.choice(CPU)) == S:
                    print("Computer chose sisscors")
                    CPUScore += 0
                    playerScore += 0
                    print(f"You Tie!\nCPU Score: {CPUScore}\nPlayer Score: {playerScore}")
                    input()
                    CPU_Active()
                    return (random.choice(CPU)), CPUScore, playerScore
                if (random.choice(CPU)) == R:
                    print("Computer chose Rock")
                    CPUScore += 1
                    playerScore += 0
                    print(f"You Lose!\nCPU Score: {CPUScore}\nPlayer Score: {playerScore}") 
                    input()
                    CPU_Active()
                    return (random.choice(CPU)), CPUScore, playerScore
                if (random.choice(CPU)) == P:
                    print("Computer chose Paper")
                    CPUScore += 0
                    playerScore +=1
                    print(f"You Win!\nCPU Score: {CPUScore}\nPlayer Score: {playerScore}") 
                    input()
                    CPU_Active()
                    return (random.choice(CPU)), CPUScore, playerScore
            




        case "m":
            os.system("cls")
            mainMenu()
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
        case _:
            input("Invalid Entry")
            CPU_Active()





#CODE- EXTING THE PROGRAM -CODE
def exit_Area():
    os.system("cls")
    match input("Type the letter 'm' to go to main menu or 'e' to exit the program:\n"):
        case 'm':
            mainMenu()
        case 'e':
            official_Goodbye()
        case _:
            input("Invalid Entry")
            exit_Area()


Funny = "You need to leave!"
Regular = "Goodbye have a nice day"
Alligator = "See ya later Alligator"


exit = (Funny, Regular, Alligator)

def official_Goodbye():
    os.system("cls")
    print(random.choice(exit))
    input()



#CODE- TUTORIAL -CODE
def tutorial():
    os.system("cls")
    match input("The way this game works is.. Im not going to explain it im just explain how I coded it you should already know.\nBassicaly all you have to do is just pick a letter and the CPU will pick one as well and whoever has the best choice will win.\n\nType m to go back to main menu:\n"):
        case 'm':
            mainMenu()
        case _:
            input("Invalid Entry")
            tutorial()

def score_Track():
    os.system("cls")
    match input(f"Player Score: {playerScore}\nCPU Score: {CPUScore}\n\nType 'm' to go to main menu:\n"):
        case "m":
            mainMenu()
        case _:
            input("Invalid Entry")
            score_Track()
            os.system("cls")






mainMenu()