 #trying tictactoe again using minimax

#  _|_|_
#  _|_|_
#   | |

# 0 is blank
# 1 is X
# -1 is O

import copy

HUMAN = 1
BOT = -1

table = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

def clean():

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def render(table):

    #this function will print the table.
    #:param: table -> the current state of the table

    displayTable = copy.deepcopy(table) #copies the current tables state into a new variable (so that the table state remains the same)
    rowCount = 0
    cellCount = 0
    
    for row in displayTable: #gets each row from the table
        for cell in row: #gets each cell from each row
            if cell == 0:
                displayTable[rowCount][cellCount] = "-" #identifies the cell and replaces it with its' respective symbol
                cellCount += 1
            elif cell == -1:
                displayTable[rowCount][cellCount] = "O"
                cellCount += 1
            elif cell == 1:
                displayTable[rowCount][cellCount] = "X"
                cellCount += 1
        if rowCount == 0:
            displayTable[0].append("A") #adds the co-ordinates onto the end (so players can identify which row to play)
        elif rowCount == 1:
            displayTable[1].append("B")
        elif rowCount == 2:
            displayTable[2].append("C")
        rowCount +=1
        cellCount = 0

    print(str(["1","2","3"]).strip('[]').replace('\'', '')) #prints each row of the table
    print(str(displayTable[0]).strip('[]').replace('\'', ''))
    print(str(displayTable[1]).strip('[]').replace('\'', ''))
    print(str(displayTable[2]).strip('[]').replace('\'', ''))

def empty_cells(table):

    #this function looks for and stores the co-ordinates of each empty cell + the number of empty cells
    #:param: table -> the current state of the table

    emptyCount = 0
    emptyCoords = [] #coords will be stored as [x,y], [column index, row index]
    rowCount = 0
    cellCount = 0


    for row in table: #gets each row from the table
        for cell in row: #gets each cell from each row
            if cell == 0: #checks if it is blank
                emptyCount +=1 #if so, it adds 1 to the counter
                emptyCoords.append([cellCount,rowCount]) #and it adds the co-ordinates
            cellCount +=1
        cellCount = 0
        rowCount +=1

    return emptyCount, emptyCoords

def initiate():
    
    #this function starts the game by asking the player wether they want to go first or second. it will return True if the player goes first, False if they go second

    initiate = True

    while initiate:
        clean()
        print("Welcome to TicTacToe By Lorand")
        turn = input("Would you like to play first, or second? (for first type 1, else type 2) - ")

        if turn == "1":
            initiate = False
            return True
        elif turn == "2":
            initiate = False
            return False
        else:
            input("Only inputs 1 or 2 are accepted! (type anything to continue) ")

def win_check(table):

    #this function looks for wins within the table. There are 8 possible wins. 3 horizontal, 3 vertical and 2 diagonal
    #
    # 0,0 | 0,1 | 0,2
    #-----------------
    # 1,0 | 1,1 | 1,2
    #-----------------
    # 2,0 | 2,1 | 2,2
    #
    #:param: table -> the current state of the table   

    if table[0][0] + table[0][1] + table[0][2] == 3 or table[0][0] + table[0][1] + table[0][2] == -3: #horizontal wins
        return True
    elif table[1][0] + table[1][1] + table[1][2] == 3 or table[1][0] + table[1][1] + table[1][2] == -3:
        return True
    elif table[2][0] + table[2][1] + table[2][2] == 3 or table[2][0] + table[2][1] + table[2][2] == -3:
        return True
    elif table[0][0] + table[1][0] + table[2][0] == 3 or table[0][0] + table[1][0] + table[2][0] == -3: #vertical wins
        return True
    elif table[0][1] + table[1][1] + table[2][1] == 3 or table[0][1] + table[1][1] + table[2][1] == -3:
        return True
    elif table[0][2] + table[1][2] + table[2][2] == 3 or table[0][2] + table[1][2] + table[2][2] == -3:
        return True
    elif table[0][0] + table[1][1] + table[2][2] == 3 or table[0][0] + table[1][1] + table[2][2] == -3: #diagonal wins
        return True
    elif table[0][2] + table[1][1] + table[2][0] == 3 or table[0][2] + table[1][1] + table[2][0] == -3:
        return True
    else: 
        return False

def game_over():

    #this function finds who won and ends the game
    print("Game over!")

def conversion(x,y):

    x = int(x)-1

    if y == "A":
        y = 0
    elif y == "B":
        y = 1
    elif y == "C":
        y = 2
    
    return x, y

def cellSelect(table):

    #This function validates a users input, then converts it to co-ordinates that identify a cell on the table
    #:param: table -> the current state of the table   

    validate = True
    xChoose = True
    yChoose = False
    emptyCheck = False


    while validate:
        while xChoose: #first the player inputs which column their cell is in.

            x = input("Please input which column you would like to play (1/2/3) - ")

            if x == "1" or x == "2" or x == "3": #here their input is validated to be a number between 1 through 3
                xChoose = False
                yChoose = True
            else:
                print(x, " was not a valid input! only inputs 1,2 or 3 are accepted.")

        while yChoose: #second the player inputs which row their cell is in.

            y = input("Please input which row you would like to play (A/B/C) - ")

            if y == "A" or y == "B" or y == "C": #here their input is validated to be a letter A B or C
                yChoose = False
                emptyCheck = True #now we now their column and row, we can identify the exact cell
            else:
                print(y, " was not a valid input! only inputs 'A','B' or 'C' are accepted.")

        while emptyCheck:

            x, y = conversion(x,y)[0], conversion(x,y)[1] #calling the function conversion() to find the coords of the cell. As conversion() returns a list with 2 numbers we need to get one at a time and add it into seperate variables
            if table[y][x] == 0: #here it confirms if their chosen cell is empty
                emptyCheck = False
                validate = False #job done, their cell has been chosen and validated

            else: #if it is not empty it will restart the entire process

                input("The cell you selected is taken. Type anything to continue ")
                clean()
                render(table)

                emptyCheck = False
                xChoose = True


    




def turnHuman(table):

    #this function asks for the humans input to place a piece, then places it.
    #:param: table -> the current state of the table

    clean()
    render(table)

    cellSelect(table)


        
    

def turnBot():
    print("Bots turn!")

def main():

    playHuman = initiate()
    gameStarted = True

    while gameStarted:
        if empty_cells(table) == 0 or win_check(table):
            gameStarted = False
            game_over()
        else:
            if playHuman:
                turnHuman()
            else:
                turnBot()




clean()
render(table)
print(empty_cells(table))
cellSelect(table)
