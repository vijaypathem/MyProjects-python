import random

# Game Board
playBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# let say player X
currentPlayer = "X"

winner = None

isGameOver = False


# display Board
def printBoard(playBoard):
    print(playBoard[0] + " | " + playBoard[1] + " | " + playBoard[2])
    print("----------")
    print(playBoard[3] + " | " + playBoard[4] + " | " + playBoard[5])
    print("----------")
    print(playBoard[6] + " | " + playBoard[7] + " | " + playBoard[8])


# take input from player and fill in valid position
def playerInput(playBoard):
    while True:
        inp = input("Enter Position (1-9): ")
        if inp == "" or not inp.isdigit():
            print("Enter Valid Position")
        else:
            inp = int(inp)
            if inp > 0 and inp < 10 and playBoard[inp - 1] == "-":
                playBoard[inp - 1] = currentPlayer
                break
            else:
                print("Enter Valid Position")


# switching player after placing position
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# check is any player won
def checkWinner():
    global winner
    global isGameOver
    if playBoard[0] == playBoard[1] == playBoard[2] and playBoard[0] != "-":
        winner = currentPlayer
        print(f"Winner is {currentPlayer} ")
        isGameOver = True
    elif playBoard[3] == playBoard[4] == playBoard[5] and playBoard[3] != "-":
        winner = currentPlayer
        print(f"Winner is {currentPlayer} ")
        isGameOver = True
    elif playBoard[6] == playBoard[7] == playBoard[8] and playBoard[6] != "-":
        winner = currentPlayer
        print(f"Winner is {currentPlayer} ")
        isGameOver = True
    elif playBoard[0] == playBoard[3] == playBoard[6] and playBoard[0] != "-":
        winner = currentPlayer
        print(f"Winner is {currentPlayer} ")
        isGameOver = True
    elif playBoard[1] == playBoard[4] == playBoard[7] and playBoard[1] != "-":
        winner = currentPlayer
        print(f"Winner is {currentPlayer} ")
        isGameOver = True
    elif playBoard[2] == playBoard[5] == playBoard[8] and playBoard[2] != "-":
        winner = currentPlayer
        print(f"Winner is {currentPlayer} ")
        isGameOver = True
    elif playBoard[0] == playBoard[4] == playBoard[8] and playBoard[0] != "-":
        winner = currentPlayer
        print(f"Winner is {currentPlayer} ")
        isGameOver = True
    elif playBoard[2] == playBoard[4] == playBoard[6] and playBoard[2] != "-":
        winner = currentPlayer
        print(f"Winner is {currentPlayer} ")
        isGameOver = True


# chech wether game is over or not
def checkTie():
    global isGameOver
    if "-" not in playBoard and winner == None:
        isGameOver = True
        print("Game Over : Tie")


def computer(playBoard):
    while True:
        inp = random.randint(0, 8)
        if playBoard[inp] == "-":
            playBoard[inp] = currentPlayer
            break


printBoard(playBoard)
while not isGameOver:
    playerInput(playBoard)
    checkWinner()
    checkTie()
    switchPlayer()
    if winner != None:
        printBoard(playBoard)
        break
    computer(playBoard)
    checkWinner()
    checkTie()
    switchPlayer()
    printBoard(playBoard)
