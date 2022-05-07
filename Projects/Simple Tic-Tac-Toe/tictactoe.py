cells = '         '
board = [[cells[0], cells[1], cells[2]],
         [cells[3], cells[4], cells[5]],
         [cells[6], cells[7], cells[8]]]
is_x = True

def print_grid() :
    print('---------')
    print('|', cells[0], cells[1], cells[2], '|')
    print('|', cells[3], cells[4], cells[5], '|')
    print('|', cells[6], cells[7], cells[8], '|')
    print('---------')
    return

def is_win(b) :
    winner = None
    for i in range(3) :
        if b[i][0] == b[i][1] == b[i][2] and b[i][0] != " " :
            winner = b[i][0]
            break
        if b[0][i] == b[1][i] == b[2][i] and b[0][i] != " " :
            winner = b[0][i]
            break
    if b[1][1] != " " :
        if (b[0][0] == b[1][1] == b[2][2]
                or b[0][2] == b[1][1] == b[2][0]) :
            winner = b[1][1]
    if winner is not None :
        print(f"{winner} wins!")
        return True
    return False

def draw(b):
    for i in b:
        for j in i:
            if j == " ":
                return False
    print("Draw")
    return True

print_grid()

while True :
    try :
        x, y = [int(x) for x in input("Enter the coordinates:").split()]
        if (x not in range(1, 4)) or (y not in range(1, 4)) :
            raise IndexError
        elif board[x - 1][y - 1] != " " :
            raise TypeError
        if is_x == True:
            board[x - 1][y - 1] = "X"
            cells = ''.join([''.join(i) for i in board])
            print_grid()
            if is_win(board) or draw(board) == True:
                break
            is_x = not is_x
        else:
            board[x - 1][y - 1] = "O"
            cells = ''.join([''.join(i) for i in board])
            print_grid()
            if is_win(board) or draw(board) == True:
                break
            is_x = True
        continue
    except ValueError :
        print("You should enter numbers!")
        continue
    except IndexError :
        print("Coordinates should be from 1 to 3!")
        continue
    except TypeError :
        print("This cell is occupied! Choose another one!")
        continue
