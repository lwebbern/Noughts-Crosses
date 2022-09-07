import random

playing = True
choosingTurn = True
turnHuman = True
gameOngoing = False
rowLocate = False
columnLocate = False
pieceLocate = False

displayRow1 = ["-","-","-","1"]
displayRow2 = ["-","-","-","2"]
displayRow3 = ["-","-","-","3"]
displayRow4 = ["A","B","C"]

amazing = True

realRow1 = [1,1,1]
realRow2 = [1,1,1]
realRow3 = [1,1,1]
vertical1 = []
vertical2 = []
vertical3 = []
diagonalUp = []
diagonalDown = []
fullList = []

displayBoard = [displayRow1,displayRow2,displayRow3]
realBoard = [realRow1, realRow3, realRow3]
fullListInfo = ["realRow1","realRow2", "realRow3", "vertical1", "vertical2", "vertical3", "diagonalDown", "diagonalUp"]

selectedListIndex = 10
selectedListCounter = 0
randomNumber = 0
timesPlayed = 0
rowInt = 0
columnInt = 0
columnIndex = 0
turnNumber = 1
totalNumFreeSpace = 0
selectedRow = displayRow4

def screenClear():
    print("\n\n\n")

def verticalDiagonalRows():

    global vertical1
    global vertical2
    global vertical3
    global diagonalDown
    global diagonalUp
    global fullList

    vertical1.append(realRow1[0])
    vertical1.append(realRow2[0])
    vertical1.append(realRow3[0])

    vertical2.append(realRow1[1])
    vertical2.append(realRow2[1])
    vertical2.append(realRow3[1])

    vertical3.append(realRow1[2])
    vertical3.append(realRow2[2])
    vertical3.append(realRow3[2])

    diagonalDown.append(realRow1[0])
    diagonalDown.append(realRow2[1])
    diagonalDown.append(realRow3[2])

    diagonalUp.append(realRow3[0])
    diagonalUp.append(realRow2[1])
    diagonalUp.append(realRow1[2])

    fullList.append(realRow1)
    fullList.append(realRow2)
    fullList.append(realRow3)
    fullList.append(vertical1)
    fullList.append(vertical2)
    fullList.append(vertical3)
    fullList.append(diagonalDown)
    fullList.append(diagonalUp)
    print(fullList)


def winCheck():

    global realRow1
    global realRow2
    global realRow3
    global vertical1
    global vertical2
    global vertical3
    global diagonalDown
    global diagonalUp
    global gameOngoing

    global verticalDiagonalRows

    verticalDiagonalRows()

    if sum(realRow1) == 27 or sum(realRow2) == 27 or sum(realRow3) == 27 or sum(vertical1) == 27 or sum(vertical2) == 27 or sum(vertical3) == 27 or sum(diagonalDown) == 27 or sum(diagonalUp) == 27:
        input("you have won the game")
        gameOngoing = False

    elif sum(realRow1) == 0 or sum(realRow2) == 0 or sum(realRow3) == 0 or sum(vertical1) == 0 or sum(vertical2) == 0 or sum(vertical3) == 0 or sum(diagonalDown) == 0 or sum(diagonalUp) == 0:
        input("you have lost the game")
        gameOngoing = False


def boardPrint():

    global realRow1
    global realRow2
    global realRow3

    global displayRow1
    global displayRow2
    global displayRow3

    print(realRow1)
    print(realRow2)
    print(realRow3)

    counter = 0
    print("you are in the function now")
    for place in realRow1:

        if str(realRow1[counter]) == '1':
            displayRow1[counter] = "-"

        elif str(realRow1[counter]) == '0':
            displayRow1[counter] = "O"

        elif str(realRow1[counter]) == '9':
            displayRow1[counter] = "X"

        if counter == 2:
            counter = 0

        counter += 1

    counter = 0
    for place in realRow2:

        if str(realRow2[counter]) == '1':
            displayRow2[counter] = "-"

        elif str(realRow2[counter]) == '0':
            displayRow2[counter] = "O"

        elif str(realRow2[counter]) == '9':
            displayRow2[counter] = "X"

        if counter == 2:
            counter = 0

        counter += 1

    counter = 0
    for place in realRow3:

        if str(realRow3[counter]) == '1':
            displayRow3[counter] = "-"
            counter += 1

        elif str(realRow3[counter]) == '0':
            displayRow3[counter] = "O"
            counter += 1

        elif str(realRow3[counter]) == '9':
            displayRow3[counter] = "X"
            counter += 1

    print(str(displayRow1).strip('[]').replace('\'', ''))
    print(str(displayRow2).strip('[]').replace('\'', ''))
    print(str(displayRow3).strip('[]').replace('\'', ''))
    print(str(displayRow4).strip('[]').replace('\'', ''))

def piecePlaceFunc(row,index):

    global turnHuman
    global rowLocate
    global piecePlace

    if row[index] == 0 or row[index] == 9:

        print("hello you are now in the first If statement, row[index] = ",row[index])
        print("turnHuman = ",turnHuman)
        piecePlace = False
        turnHuman = True
        rowLocate = True

        input("There is already a piece there, please type anything to try again - ")
        print(row)
        print(index)
        print(row[index])



    elif row[index] == 1:
        print("hello row[index] = ",row[index])
        if turnHuman:
            row[index] = 9
            winCheck()
            piecePlace = False
            turnHuman = False
        elif turnHuman == False:
            row[index] = 0
            winCheck()
            piecePlace = False
            turnHuman = True

def botMoveAlgorithm():

    global columnIndex
    global selectedRow
    global piecePlace
    global verticalDiagonalRows
    global counter
    global totalNumFreeSpace
    global selectedListIndex

    counter = 0
    selectedListCounter = 0
    verticalDiagonalRows()

    if turnNumber == 1:
        selectedRow = realRow1
        columnIndex = 0
        piecePlace = True

    elif turnNumber == 2:
        if realRow1[0]== 9 or realRow1[2]== 9 or realRow3[0]== 9 or realRow3[2]== 9:
            print("realRow1[0] = {0} | realRow1[2] = {1} | realRow3[0] = {2} | realRow3[2] = {3}".format(realRow1[0], realRow1[2], realRow3[0], realRow3[2]))
            selectedRow = realRow2
            columnIndex = 1
            piecePlace = True

        else:
            print("it went to else")
            selectedRow = realRow1
            columnIndex = 0
            piecePlace = True

    else:
        for list in fullList:
            if sum(list) == 19:
                for item in list:
                    if item == 1:
                        if fullListInfo[selectedListCounter] == "vertical1":
                            print("poo")
                        columnIndex = counter
                        selectedRow = list
                        totalNumFreeSpace += 1
                    else:
                        counter +=1
            else:
                selectedListCounter += 1

        if totalNumFreeSpace == 0:
            print("poo2")

    print(totalNumFreeSpace)






while playing:
    screenClear()
    boardPrint()

    while choosingTurn == True:
        if timesPlayed == 0:
            randomNumber = random.randint(0,1)

            if randomNumber <= 0.5:
                turnHuman = True
                print("You will be playing X, you go first")

            elif randomNumber > 0.5:
                turnHuman = False
                input("You will be playing O, you go second (type anything to continue) ")

            choosingTurn = False
            gameOngoing = True
            rowLocate = True

        else:
            turnHuman = turnHuman

            if turnHuman:
                print("You will be playing X, you go first")
            else:
                input("You will be playing O, you go second (type anything to continue) ")

            choosingTurn = False
            gameOngoing = True
            rowLocate = True

    while gameOngoing:
        input("bot has made its move gameOngoing")
        while turnHuman:
            input("bot has made its move turnHuman")
            while rowLocate:
                print("you are locating a row")
                rowMove = input("Please enter the row you would like to place your on (1,2,3) - ")

                try:
                    rowInt = int(rowMove)
                    if rowMove == '1':
                        selectedRow = realRow1
                        rowLocate = False
                        columnLocate = True

                    elif rowMove == '2':
                        selectedRow = realRow2
                        rowLocate = False
                        columnLocate = True

                    elif rowMove == '3':
                        selectedRow = realRow3
                        rowLocate = False
                        columnLocate = True

                    else:
                        input("you typed '{0}', please make sure it is a number on the board (type anything to continue) - ".format(rowMove))
                        screenClear()
                        boardPrint()


                except ValueError:
                    input("you typed '{0}', please make sure it is a number on the board (type anything to continue) - ".format(rowMove))
                    screenClear()
                    boardPrint()

            while columnLocate:
                columnMove = input("Please enter the column you would like to place your piece on (A,B,C) - ")

                try:
                    columnInt = int(columnMove)
                    input("you typed '{0}', please make sure it is a letter on the board (type anything to continue) - ".format(columnMove))
                    screenClear()
                    boardPrint()

                except ValueError:
                    if columnMove == "A":
                        columnIndex = 0
                        columnLocate = False
                        piecePlace = True
                        print("hello u are in human turn piece place")

                    elif columnMove == "B":
                        columnIndex = 1
                        columnLocate = False
                        piecePlace = True

                    elif columnMove == "C":
                        columnIndex = 2
                        pieceLocate = True
                        columnLocate = False
                        piecePlace = True

                    else:
                        input("you typed '{0}', please make sure it is a letter on the board (type anything to continue) - ".format(columnMove))
                        screenClear()
                        boardPrint()

            while piecePlace:
                print("\nyou are in PiecePlace: of turnHuman")
                piecePlaceFunc(selectedRow, columnIndex)
                screenClear()
                boardPrint()


                turnNumber += 1

        while turnHuman == False:

            botMoveAlgorithm()



            piecePlaceFunc(selectedRow, columnIndex)
            screenClear()
            boardPrint()
            turnNumber += 1
            input("bot has made its move")
            rowLocate = True

