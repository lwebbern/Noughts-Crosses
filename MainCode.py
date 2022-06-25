# bot will always play O

# 0 is blank
# 1 is X
# -1 is O

#  A1|A2|A3
#  B1|B2|B3
#  C1|C2|C3
# ^each cell in the tictactoe table is labelled with co-ordinates this way

#  0|1|2
#  3|4|5
#  6|7|8
# ^these are the corresponding indexes in fullLogicTable for each cell of the tictactoe table

fullLogicTable = [0,0,0,0,0,0,0,0,0]
fullDisplayTable = []
currentDisplayCell = ""
counter = 0
displayRowNum = ["1","2","3"]
displayRowA = []
displayRowB = []
displayRowC = []

def displayTable(fullLogicTable): #function to turn the logic table into the actual tictactoe displayable table, then display it row by row.

    counter = 0
    fullDisplayTable = [] #list that will contain all the X's and O's
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

def evaluatePosition(fullLogicTable,Maximizer):

    if Maximizer == True:  
        



displayTable(fullLogicTable)
cellIndex = cellIndexFinder("A","3")
print(cellIndex)
