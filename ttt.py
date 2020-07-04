import random


# Function to create the board based on the size provided by the user
def createboard():
    global board
    board = list(range(0, size ** 2))
    for i in range(0, size ** 2):
        board[i] = i
    showboard()


# Function to show the status of the board
def showboard():
    z = 0
    for x in range(0, size):
        for y in range(0, size):
            if y == size - 1:
                print(board[z])
            else:
                print(board[z], end=" | ")
            z += 1
        print('---------')


# Function to check if the winning condition is achieved
# Generates all winning conditions based on the size of board
def checkwin(move):
    movelist = []
    x = 0
    # Generating winning condition for each row
    while x < size ** 2:
        moves = []
        for i in range(size):
            moves.append(board[x])
            x += 1
        movelist.append(moves)
    # Generating winning condition for each column
    x = 0
    while x < size ** 2:
        for i in range(size):
            moves = []
            for j in range(size):
                moves.append(board[i + j * size])
                x += 1
            movelist.append(moves)
    # Generating winning condition for diagonal
    moves = []
    for i in range(size):
        moves.append(board[i * size + i])
    movelist.append(moves)
    drawcount = 0
    # Checking if winning condition is achieved
    for i in movelist:
        if move in i and len(i) > 0 and all(elem == i[0] for elem in i):
            return True
    for i in range(size**2):
        if board[i] != i:
            drawcount += 1
    if drawcount == size**2:
        showboard()
        inp = input("Game ended in a draw!! Do you want to continue?(Y/N)")
        if inp == 'Y':
            main()


# Main method is called for starting the game. It is also called when the game ends in a draw.
def main():
    global size
    try:
        size = int(input("Enter size of board:"))
    except:
        print("Please enter a number!!!")
    createboard()
    while True:
        try:
            move = int(input("Select a Spot: "))
        except:
            print("Please enter a number!!!")
        if move >= size ** 2:
            print('Invalid Move')
            continue
        if board[move] != 'O' and board[move] != 'X':
            print("Player takes ",str(move))
            board[move] = 'X'
            if checkwin('X'):
                print('Player Wins')
                showboard()
                break
            while True:
                random.seed()
                comp = random.randint(0, size ** 2 - 1)
                if board[comp] != 'X' and board[comp] != 'O':
                    print("Computer takes ", str(comp))
                    board[comp] = 'O'
                    showboard()
                    if checkwin('O'):
                        print("Computer Wins")
                        showboard()
                        exit()
                    break
                else:
                    continue
        else:
            print("Position is already taken. Try Again!!!")
            continue


if __name__ == "__main__":
    main()
