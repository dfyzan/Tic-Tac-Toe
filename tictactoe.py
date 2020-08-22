o_wins = False
x_wins = False
no_empty = False
o_move = False


def creating_matrix(input_string):
    pos = []
    n = 0
    # creating matrix
    # [[0,0; 0,1; 0,2],
    #  [1,0; 1,1; 1,2],
    #  [2,0; 2,1; 2,2]]
    for i in range(9):
        if i % 3 == 0:
            pos.append([])
            if not i == 0:
                n += 1
        try:
            pos[n].append(input_string[i])
        except IndexError:
            pos.append(input_string[i])
    return pos


def print_position():
    pos = position
    print('---------')
    for x in range(3):
        print('|', end=' ')
        for y in range(3):
            print(pos[x][y], end=' ')
        print('|')
    print('---------')


def check_for_win():
    pos = position
    o_win = False
    x_win = False
    for x in range(3):
        # checking for horizontal lines
        if pos[x][0] == pos[x][1] == pos[x][2] == 'X':
            x_win = True
        elif pos[x][0] == pos[x][1] == pos[x][2] == 'O':
            o_win = True

        # checking for vertical lines
        if pos[0][x] == pos[1][x] == pos[2][x] == 'X':
            x_win = True
        elif pos[0][x] == pos[1][x] == pos[2][x] == 'O':
            o_win = True

        # checking for diagonals
        if pos[0][0] == pos[1][1] == pos[2][2] == 'X':
            x_win = True
        elif pos[0][0] == pos[1][1] == pos[2][2] == 'O':
            o_win = True
        if pos[0][2] == pos[1][1] == pos[2][0] == 'X':
            x_win = True
        elif pos[0][2] == pos[1][1] == pos[2][0] == 'O':
            o_win = True
    return o_win, x_win


def printing_results():
    o_win, x_win = check_for_win()
    if o_win:
        print('O wins')
    elif x_win:
        print('X wins')
    elif there_is_no_empty():
        print('Draw')


def there_is_no_empty():
    pos = position
    num_empty = sum(x.count('_') for x in pos)
    if num_empty == 0:
        return True


def is_finished():
    o_win, x_win = check_for_win()
    if o_win or x_win or there_is_no_empty():
        return True


def is_valid(coordinates):
    try:
        if 1 <= int(coordinates[0]) <= 3 and 1 <= int(coordinates[2]) <= 3:
            # converting coords from
            #       (1, 3) (2, 3) (3, 3)  to  [[0,0; 0,1; 0,2],
            #       (1, 2) (2, 2) (3, 2)       [1,0; 1,1; 1,2],
            #       (1, 1) (2, 1) (3, 1)       [2,0; 2,1; 2,2]]
            if not position[abs(int(coordinates[2]) - 3)][int(coordinates[0]) - 1] == '_':
                return 'Occupied'
            return 'ok'
        else:
            return 'Out of range'
    except ValueError:
        return 'Non num'


# creating empty matrix
position = creating_matrix('_________')
code = 'ok'

while not is_finished():
    if code == 'ok':
        print_position()
    coords = input('Enter the coordinates: > ')
    code = is_valid(coords)
    if code == 'Out of range':
        print('Coordinates should be from 1 to 3!')
    elif code == 'Non num':
        print('You should enter numbers!')
    elif code == 'Occupied':
        print('This cell is occupied! Choose another one!')
    else:
        if o_move:
            position[abs(int(coords[2]) - 3)][int(coords[0]) - 1] = 'O'
            o_move = False
        else:
            position[abs(int(coords[2]) - 3)][int(coords[0]) - 1] = 'X'
            o_move = True

print_position()
printing_results()

d = input()
