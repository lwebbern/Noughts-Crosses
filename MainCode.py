# bot will always play O

# 0 is blank
# 1 is X
# -1 is O

# test

#  A1|A2|A3
#  B1|B2|B3
#  C1|C2|C3
# ^each cell in the tictactoe table is labelled with co-ordinates this way

#  0|1|2
#  3|4|5
#  6|7|8
# ^these are the corresponding indexes in fullLogicTable for each cell of the tictactoe table


import random


fullLogicTable = [0,0,0,0,0,0,0,0,0]
fullDisplayTable = []
currentDisplayCell = ""
counter = 0
maxCount = 0
displayRowNum = ["1","2","3"]
displayRowA = []
displayRowB = []
displayRowC = []
checking = False
piece = 1



def displayTable(fullLogicTable): #function to turn the logic table into the actual tictactoe displayable table, then display it row by row.

    counter = 0
    fullDisplayTable = [] #list that will contain all the X's and O's
    displayRowA = []
    displayRowB = []
    displayRowC = []
    for cell in fullLogicTable: #goes cell by cell in the fullLogicTable list to convert 0's into ' ', 1's into 'X' and 2's into 'O'

        if cell == 0:  #turns 0 into " "
            currentDisplayCell = "-"
        elif cell == 1:  #turns 1 into "X"
            currentDisplayCell = "X"
        elif cell == -1:  #turns 2 into "O"
            currentDisplayCell = "O"
    
        fullDisplayTable.insert(counter, currentDisplayCell) #end result is a table fully converted. now it just needs to be displayed row by row.
        counter = counter +1 
    
    counter = 0

    for cell in fullDisplayTable: #goes through each cell to then change the corresponding cell in each row. This way i can then print each row seperately.
        
        if counter >= 6 and counter <9: #the last 3 values (counter goes from 6-8) will be added to rowB. logic has to be structured this way as the counter gets updated in each loop.
            displayRowC.append(cell)
            counter += 1 

        if counter >= 3 and counter <6: #the second 3 values (counter goes from 3-5) will be added to rowB
            displayRowB.append(cell)
            counter += 1   

        if counter < 3: #the first 3 values (counter goes from 0-2) will be added to rowA
            displayRowA.append(cell)
            counter += 1

    displayRowA.append("A") #it adds the co-ordinate of each row at the end.
    displayRowB.append("B")
    displayRowC.append("C")

    print(str(displayRowNum).strip('[]').replace('\'', '')) #displays each row without [], and removes the '' from each string in list. 
    print(str(displayRowA).strip('[]').replace('\'', ''))
    print(str(displayRowB).strip('[]').replace('\'', ''))
    print(str(displayRowC).strip('[]').replace('\'', ''))



def cellIndexFinder(letter, number): #converts inputted co-ordinates (e.g A, 1) into the index that it corresponds to in the fullLogicTable. this way i can easily change values based on inputs.

    cellJoined = letter+number #converts both inputs into one string to make identification easier

    if cellJoined == "A1": #finds the corresponding index
        cellIndex = 0
    if cellJoined == "A2":
        cellIndex = 1
    if cellJoined == "A3":
        cellIndex = 2
    if cellJoined == "B1":
        cellIndex = 3
    if cellJoined == "B2":
        cellIndex = 4
    if cellJoined == "B3":
        cellIndex = 5
    if cellJoined == "C1":
        cellIndex = 6
    if cellJoined == "C2":
        cellIndex = 7   
    if cellJoined == "C3":
        cellIndex = 8   

    return cellIndex #returns the index value that i can then store in a variable.



def humanTurn():
    
    turnActive = True
    
    while turnActive: #starts the loop of placing a piece (this is so if there is a miss-input it will restart the questions again)
        numberActive = True
        displayTable(fullLogicTable)

        while numberActive: #starts the loop of asking the number question, same as above, it is so it can ask the question again if they miss-input
            number = input("Please input a number (1/2/3) - ") #stores inputted number in this variable

            if number == "1" or number == "2" or number == "3": #confirms the input is valid
                letterActive = True

                while letterActive: #starts the loop of asking the letter question, same as above, it is so it can ask the question again if they miss-input
                    letter = input("Please input a letter (A/B/C) - ").upper()
                    
                    if letter == "A" or letter == "B" or letter == "C": #confirms the input is valid
                        cell = cellIndexFinder(letter, number) #uses the cellIndexFinder() to find the index in which to place their piece.

                        if fullLogicTable[cell] == 0: #makes sure there is no piece already in that index
                            fullLogicTable[cell] = 1 #once everything is clear, it will change the 0 in that index to 1 (an X).
                            displayTable(fullLogicTable)
                            letterActive = False #ends the loop.
                            turnActive = False
                            return fullLogicTable
                        
                        else:
                            letterActive = False
                            numberActive = False
                            input("The chosen place already has a piece there! Please try again (type anything to continue) - ")
                    
                    else:
                        input("{0} is not a valid input. Please try again (type anything to continue) - ".format(letter))
            
            else:
                input("{0} is not a valid input. Please try again (type anything to continue) - ".format(number))



def evaluatePosition(fullLogicTable, player): #finds the number of X's in the same row/ column / diagonal. (Checks 8 in total, 3 rows, 3 columns, 2 diagonals)

    counter = 0 #keeps track of X's in each row individually
    maxCount = 0 #logs the highest achieved count (max is 3)
    highestCountLocation = [] #will store the indexes of the cells in the row with the max count

    if player == True: #player being True means it will evaluate the players position (X)
        piece = 1 #will now check if cells are X
    else:
        piece = -1 #will now check if cells are O

    # top row
    if fullLogicTable[0] == piece: #checks each cell of the first row individually (3 cells), everytime an X/O appears, it will add to the counter
        counter += 1
    if fullLogicTable[1] == piece:
        counter += 1
    if fullLogicTable[2] == piece:
        counter += 1
    
    if counter > maxCount: #checks if there is a new highest count
        if abs(fullLogicTable[0] + fullLogicTable[1] + fullLogicTable[2]) == counter: #checks if there are enemy player pieces in the mix. As O is -1 and X is 1.
            highestCountLocation = [0,1,2]
            maxCount = counter #if all conditions are met, it will set a new highest counter and then go through this cycle again 7 times.
            print(maxCount)
    
    counter = 0

    # middle row
    if fullLogicTable[3] == piece:
        counter += 1
    if fullLogicTable[4] == piece:
        counter += 1
    if fullLogicTable[5] == piece:
        counter += 1
    
    if counter > maxCount:
        if abs(fullLogicTable[3] + fullLogicTable[4] + fullLogicTable[5]) == counter:
            highestCountLocation = [3,4,5]
            maxCount = counter
            print(maxCount)
    
    counter = 0

    # bottom row        
    if fullLogicTable[6] == piece:
        counter += 1
    if fullLogicTable[7] == piece:
        counter += 1
    if fullLogicTable[8] == piece:
        counter += 1
    
    if counter > maxCount:
        if abs(fullLogicTable[6] + fullLogicTable[7] + fullLogicTable[8]) == counter:
            highestCountLocation = [6,7,8]
            maxCount = counter
            print(maxCount)
    
    counter = 0

    # left column      
    if fullLogicTable[0] == piece:
        counter += 1
    if fullLogicTable[3] == piece:
        counter += 1
    if fullLogicTable[6] == piece:
        counter += 1
    
    if counter > maxCount:
        if abs(fullLogicTable[0] + fullLogicTable[3] + fullLogicTable[6]) == counter:
            highestCountLocation = [0,3,6]
            maxCount = counter
            print(maxCount)
    
    counter = 0

    # middle column       
    if fullLogicTable[1] == piece:
        counter += 1
    if fullLogicTable[4] == piece:
        counter += 1
    if fullLogicTable[7] == piece:
        counter += 1
    
    if counter > maxCount:
        if abs(fullLogicTable[1] + fullLogicTable[4] + fullLogicTable[7]) == counter:
            highestCountLocation = [1,4,7]
            maxCount = counter
            print(maxCount)

    counter = 0

    # right column       
    if fullLogicTable[2] == piece:
        counter += 1
    if fullLogicTable[5] == piece:
        counter += 1
    if fullLogicTable[8] == piece:
        counter += 1
    
    if counter > maxCount:
        if abs(fullLogicTable[2] + fullLogicTable[5] + fullLogicTable[8]) == counter:
            highestCountLocation = [2,5,8]
            maxCount = counter
            print(maxCount)

    counter = 0

    # right diagonal       
    if fullLogicTable[0] == piece:
        counter += 1
    if fullLogicTable[4] == piece:
        counter += 1
    if fullLogicTable[8] == piece:
        counter += 1
    
    if counter > maxCount:
        if abs(fullLogicTable[0] + fullLogicTable[4] + fullLogicTable[8]) == counter:
            highestCountLocation = [0,4,8]
            maxCount = counter
            print(maxCount)
    
    counter = 0

    # left diagonal        
    if fullLogicTable[2] == piece:
        counter += 1
    if fullLogicTable[4] == piece:
        counter += 1
    if fullLogicTable[6] == piece:
        counter += 1
    
    if counter > maxCount:
        if abs(fullLogicTable[2] + fullLogicTable[4] + fullLogicTable[6]) == counter:
            highestCountLocation = [2,4,6]
            maxCount = counter
            print(maxCount)


    return maxCount, highestCountLocation #returns the highest count it got to, plus the indexes of the cells in the row which had the count.

        
#input("are you ready to play? type anything to continue - ")
#if random.randint(1,2) == 1:


displayTable(fullLogicTable)
cellIndex = cellIndexFinder("A","3")
print(evaluatePosition(fullLogicTable, True))

humanTurn()
