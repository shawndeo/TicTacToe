Space1 = '1'
Space2 = '2'
Space3 = '3'
Space4 = '4'
Space5 = '5'
Space6 = '6'
Space7 = '7'
Space8 = '8'
Space9 = '9'

def resetBoard():
    global Space1
    Space1 = '1'
    global Space2
    Space2 = '2'
    global Space3
    Space3 = '3'
    global Space4
    Space4 = '4'
    global Space5
    Space5 = '5'
    global Space6
    Space6 = '6'
    global Space7
    Space7 = '7'
    global Space8
    Space8 = '8'
    global Space9
    Space9 = '9'

occupiedSpace = 'Pick an unoccupied space!'
winMessageP1 = 'Player 1 won! \n'
winMessageP2 = 'Player 2 won! \n'

def showBoard():
    print(f'{Space1} | {Space2} | {Space3}')
    print(f'{Space4} | {Space5} | {Space6}')
    print(f'{Space7} | {Space8} | {Space9}')

def pickSpaceP1():
    turn = input('Pick a space: ')
    global Space1
    global Space2
    global Space3
    global Space4
    global Space5
    global Space6
    global Space7
    global Space8
    global Space9
    if turn == '1':
        if Space1 != 'x' and Space1 != 'o':
            Space1 = 'x'
        else:
            print(occupiedSpace)
    if turn == '2':
        if Space2 != 'x' and Space2 != 'o':
            Space2 = 'x'
        else:
            print(occupiedSpace)
    if turn == '3':
        if Space3 != 'x' and Space3 != 'o':
            Space3 = 'x'
        else:
            print(occupiedSpace)
    if turn == '4':
        if Space4 != 'x' and Space4 != 'o':
            Space4 = 'x'
        else:
            print(occupiedSpace)
    if turn == '5':
        if Space5 != 'x' and Space5 != 'o':
            Space5 = 'x'
        else:
            print(occupiedSpace)
    if turn == '6':
        if Space6 != 'x' and Space6 != 'o':
            Space6 = 'x'
        else:
            print(occupiedSpace)
    if turn == '7':
        if Space7 != 'x' and Space7 != 'o':
            Space7 = 'x'
        else:
            print(occupiedSpace)
    if turn == '8':
        if Space8 != 'x' and Space8 != 'o':
            Space8 = 'x'
        else:
            print(occupiedSpace)
    if turn == '9':
        if Space9 != 'x' and Space9 != 'o':
            Space9 = 'x'
        else:
            print(occupiedSpace)
    showBoard()

def pickSpaceP2():
    turn = input('Pick a space: ')
    global Space1
    global Space2
    global Space3
    global Space4
    global Space5
    global Space6
    global Space7
    global Space8
    global Space9
    if turn == '1':
        if Space1 != 'x' and Space1 != 'o':
            Space1 = 'o'
        else:
            print(occupiedSpace)
            pickSpaceP2()
    if turn == '2':
        if Space2 != 'x' and Space2 != 'o':
            Space2 = 'o'
        else:
            print(occupiedSpace)
    if turn == '3':
        if Space3 != 'x' and Space3 != 'o':
            Space3 = 'o'
        else:
            print(occupiedSpace)
    if turn == '4':
        if Space4 != 'x' and Space4 != 'o':
            Space4 = 'o'
        else:
            print(occupiedSpace)
    if turn == '5':
        if Space5 != 'x' and Space5 != 'o':
            Space5 = 'o'
        else:
            print(occupiedSpace)
    if turn == '6':
        if Space6 != 'x' and Space6 != 'o':
            Space6 = 'o'
        else:
            print(occupiedSpace)
    if turn == '7':
        if Space7 != 'x' and Space7 != 'o':
            Space7 = 'o'
        else:
            print(occupiedSpace)
    if turn == '8':
        if Space8 != 'x' and Space8 != 'o':
            Space8 = 'o'
        else:
            print(occupiedSpace)
    if turn == '9':
        if Space9 != 'x' and Space9 != 'o':
            Space9 = 'o'
        else:
            print(occupiedSpace)

    showBoard()

def checkWinP1():
    global Space1
    global Space2
    global Space3
    global Space4
    global Space5
    global Space6
    global Space7
    global Space8
    global Space9
    if Space1 == 'x' and Space2 == 'x' and Space3 == 'x':
        print(winMessageP1)
        main()
    if Space4 == 'x' and Space5 == 'x' and Space6 == 'x':
        print(winMessageP1)
        main()
    if Space7 == 'x' and Space8 == 'x' and Space9 == 'x':
        print(winMessageP1)
        main()
    if Space1 == 'x' and Space4 == 'x' and Space7 == 'x':
        print(winMessageP1)
        main()
    if Space2 == 'x' and Space5 == 'x' and Space8 == 'x':
        print(winMessageP1)
        main()
    if Space1 == 'x' and Space5 == 'x' and Space9 == 'x':
        print(winMessageP1)
        main()
    if Space3 == 'x' and Space5 == 'x' and Space7 == 'x':
        print(winMessageP1)
        main()

def checkWinP2():
    global Space1
    global Space2
    global Space3
    global Space4
    global Space5
    global Space6
    global Space7
    global Space8
    global Space9
    if Space1 == 'o' and Space2 == 'o' and Space3 == 'o':
        print(winMessageP2)
        main()
    if Space4 == 'o' and Space5 == 'o' and Space6 == 'o':
        print(winMessageP2)
        main()
    if Space7 == 'o' and Space8 == 'o' and Space9 == 'o':
        print(winMessageP2)
        main()
    if Space1 == 'o' and Space4 == 'o' and Space7 == 'o':
        print(winMessageP2)
        main()
    if Space2 == 'o' and Space5 == 'o' and Space8 == 'o':
        print(winMessageP2)
        main()
    if Space1 == 'o' and Space5 == 'o' and Space9 == 'o':
        print(winMessageP2)
        main()
    if Space3 == 'o' and Space5 == 'o' and Space7 == 'o':
        print(winMessageP2)
        main()

def main():
    resetBoard()

    showBoard()

    pickSpaceP1()

    pickSpaceP2()

    pickSpaceP1()

    pickSpaceP2()

    pickSpaceP1()

    checkWinP1()

    pickSpaceP2()

    checkWinP2()

    pickSpaceP1()

    checkWinP1()

    pickSpaceP2()

    checkWinP2()

    pickSpaceP1()

    checkWinP1()

main()