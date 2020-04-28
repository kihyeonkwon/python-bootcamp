def display_board(board):

    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])


def selectHorse():
    global horse1
    global horse2
    b = 0
    while b < 1:
        a = input("Player 1, select O or X")
        if a == 'O':
            horse1 = 'O'
            horse2 = 'X'
            b += 1
            print(f'Player 1 plays {horse1}, Player 2 plays {horse2}')
        elif a == 'X':
            horse1 = 'X'
            horse2 = 'O'
            b += 1
            print(f'Player 1 plays {horse1}, Player 2 plays {horse2}')
        else:
            print("Please type 'O' or 'X'.")


def player1turn():
    b = 0
    while b < 1:
        a = int(input("Player 1, where?"))
        if a < 10 and a > 0:

            if board[a] == " ":
                board[a] = horse1
                b += 1
            else:
                print("Cell is already taken")
        else:
            print("Select between 1~9")


def player2turn():
    b = 0
    while b < 1:
        a = int(input("Player 2, where?"))
        if a < 10 and a > 0:

            if board[a] == " ":
                board[a] = horse2
                b += 1
            else:
                print("Cell is already taken")
        else:
            print("Select between 1~9")


win = 0


def checkWinner():
    global win
    if board[1] == board[2] == board[3] == horse1 or board[4] == board[5] == board[6] == horse1 or board[7] == board[8] == board[9] == horse1 or board[1] == board[4] == board[7] == horse1 or board[2] == board[5] == board[8] == horse1 or board[3] == board[6] == board[9] == horse1 or board[3] == board[5] == board[7] == horse1 or board[1] == board[5] == board[9] == horse1:
        print("Player 1 is the winner!")
        win += 1

    elif board[1] == board[2] == board[3] == horse2 or board[4] == board[5] == board[6] == horse2 or board[7] == board[8] == board[9] == horse2 or board[1] == board[4] == board[7] == horse2 or board[2] == board[5] == board[8] == horse2 or board[3] == board[6] == board[9] == horse2 or board[3] == board[5] == board[7] == horse2 or board[1] == board[5] == board[9] == horse2:
        print("Player 2 is the winner!")
        win += 1
    else:
        pass


board = ['empty', ' ', ' ', ' ', ' ', ' ',  ' ', ' ',
         ' ', ' ']

selectHorse()

win = 0
round = 0
display_board(board)
while win < 1:
    round += 1
    player1turn()
    display_board(board)
    checkWinner()
    if win == 1:
        break
    if round == 5:
        print("Draw")
        break
    player2turn()
    display_board(board)
    checkWinner()
