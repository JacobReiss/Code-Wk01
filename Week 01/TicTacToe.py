import os

# This is the list the will make it so the user input value keeps
board = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

def main():
    count = 0
    
    # This is the loop that will run the code
    while count != 10:
        
        # Clears the screen 
        if count != 10:
            os.system("cls" if os.name == "nt" else "clear")
        createBoard(board)
        
        # This loops checks the availability of a space without clearing the board
        test = 1
        while test == 1:
            print()
            if checkWin() == 1:
                print ("X Wins")
                count = 10
                test = 2
            elif checkWin() == 2:
                print ("Y Wins")
                count = 10
                test = 2
            elif checkWin() == 0 and count == 9:
                print ("It's a tie")
                count = 10
                test = 2
            else:
                # Get the player input
                place = getPlayerInput(count)
                print()
            
                # This makes sure the value entered is an integer and within the range of the list
                if str.isdigit(place) and int(place) in board:
                    player = count % 2 + 1
                    if not board[int(place)] in {"X", "O"}:
                        count+=1
                        board[int(place)] = playerTurn(count)
                        print()
                        test = 2
                    else:
                        print (f"That space is already used. Try again Player {player}")
                else:
                    print (f"Input Invalid. Try again Player {player}")
                    print()
    
        
# This gets the player's input
def getPlayerInput(count):
    player = count % 2 + 1
    playLetter = count + 1
    choice = input(f"PLAYER {player}: Place an {playerTurn(playLetter)} on any square (1-9) --> ")
    return choice

# Determines which player's turn it is
# This allows it to pt either an X or O
def playerTurn(turn):
    if turn % 2 == 0: return "O"
    else: return "X"
    
# Creates the playing board with the list at the top of the code
def createBoard(board):
    print (f"{board[1]}|{board[2]}|{board[3]}")
    print ("-+-+-")
    print (f"{board[4]}|{board[5]}|{board[6]}")
    print ("-+-+-")
    print (f"{board[7]}|{board[8]}|{board[9]}")
    
# This checks the availability of a space
def checkSpace():
    if board[1] == "X" or board[1] == "Y":
        return 1
    
# This checks the win conditions to determine if anyone wins
def checkWin():
    # X win conditions
    if board[1] == "X" and board[2] == "X" and board[3] == "X":
        return 1
    elif board[4] == "X" and board[5] == "X" and board[6] == "X": 
        return 1
    elif board[7] == "X" and board[8] == "X" and board[9] == "X":
        return 1
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        return 1
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        return 1
    elif board[3] == "X" and board[6] == "X" and board[9] == "X":
        return 1
    elif board[1] == "X" and board[5] == "X" and board[9] == "X":
        return 1 
    elif board[3] == "X" and board[5] == "X" and board[9] == "X":
        return 1
    # Y win conditions
    elif board[1] == "O" and board[2] == "O" and board[3] == "O":
        return 2
    elif board[4] == "O" and board[5] == "O" and board[6] == "O":
        return 2
    elif board[7] == "O" and board[8] == "O" and board[9] == "O":
        return 2
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        return 2
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        return 2
    elif board[3] == "O" and board[6] == "O" and board[9] == "O": 
        return 2
    elif board[1] == "O" and board[5] == "O" and board[9] == "O":
        return 2
    elif board[3] == "O" and board[5] == "O" and board[9] == "O":
        return 2
    # If no win conditions are met
    else:
        return 0
        print()
    
    
# Call the main() function
main()