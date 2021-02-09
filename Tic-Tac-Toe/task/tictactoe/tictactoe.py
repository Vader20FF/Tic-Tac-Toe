def printGrid():
    global signList
    print("---------")
    print("| " + str(signList[0]) + " " + str(signList[1]) + " " + str(signList[2]) + " |")
    print("| " + str(signList[3]) + " " + str(signList[4]) + " " + str(signList[5]) + " |")
    print("| " + str(signList[6]) + " " + str(signList[7]) + " " + str(signList[8]) + " |")
    print("---------")


def validateCoordinates(x, y):
    if x < 1 or x > 3 or y < 1 or y > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    elif type(x) != int or type(y) != int:
        print("You should enter numbers!")
        return False
    else:
        return True


def whichGrid(x, y):
    global signList
    if x == 1:
        if y == 1:
            return signList[0]
        elif y == 2:
            return signList[3]
        elif y == 3:
            return signList[6]
    elif x == 2:
        if y == 1:
            return signList[1]
        elif y == 2:
            return signList[4]
        elif y == 3:
            return signList[7]
    if x == 3:
        if y == 1:
            return signList[2]
        elif y == 2:
            return signList[5]
        elif y == 3:
            return signList[8]


def whichGridNumber(x, y):
    if x == 1:
        if y == 1:
            return 0
        elif y == 2:
            return 3
        elif y == 3:
            return 6
    elif x == 2:
        if y == 1:
            return 1
        elif y == 2:
            return 4
        elif y == 3:
            return 7
    if x == 3:
        if y == 1:
            return 2
        elif y == 2:
            return 5
        elif y == 3:
            return 8


def isOccupied(gridCell):
    if gridCell == "X" or gridCell == "O":
        return True
    else:
        return False


def addSign(x, y):
    global signList
    signList[whichGridNumber(x, y)] = "X"


def gameFinished():
    global signList
    if (signList[0] == signList[1] == signList[2] == "X" or
            signList[3] == signList[4] == signList[5] == "X" or
            signList[6] == signList[7] == signList[8] == "X" or
            signList[0] == signList[3] == signList[6] == "X" or
            signList[1] == signList[4] == signList[7] == "X" or
            signList[2] == signList[5] == signList[8] == "X" or
            signList[0] == signList[4] == signList[8] == "X" or
            signList[2] == signList[4] == signList[6] == "X"):
        print("X wins")
        return True
    elif (signList[0] == signList[1] == signList[2] == "O" or
            signList[3] == signList[4] == signList[5] == "O" or
            signList[6] == signList[7] == signList[8] == "O" or
            signList[0] == signList[3] == signList[6] == "O" or
            signList[1] == signList[4] == signList[7] == "O" or
            signList[2] == signList[5] == signList[8] == "O" or
            signList[0] == signList[4] == signList[8] == "O" or
            signList[2] == signList[4] == signList[6] == "O"):
        print("O wins")
        return True
    elif all([sign != " " for sign in signList]):
        print("Draw")
        return True


signList = []
for sign in range(0, 9):
    signList.append(" ")

printGrid()

x, y = input("Enter the coordinates: ").split()
x = int(x)
y = int(y)

while not gameFinished():
    while not validateCoordinates(x, y):
        x, y = input("Enter the coordinates: ").split()
        x = int(x)
        y = int(y)

    while isOccupied(whichGrid(x, y)):
        print("This cell is occupied! Choose another one!")
        x, y = input("Enter the coordinates: ").split()
        x = int(x)
        y = int(y)

        while not validateCoordinates(x, y):
            x, y = input("Enter the coordinates: ").split()
            x = int(x)
            y = int(y)

    addSign(x, y)

    printGrid()




