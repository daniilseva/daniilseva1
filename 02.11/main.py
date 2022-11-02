def rules():
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
def play():
    return input("\nAre you reade to play the game? [Y]es or [N]o.\t").upper().startswith('Y')
def names():
    p1_name = input("\n Enter NAME of PLAYER 1\t").capitalize()
    p2_name = input("\n Enter NAME of PLAYER 2\t").capitalize()
    return (p1_name, p2_name)

def choise():
    p1_choise = ''
    p2_choise = ''
    while p1_choise != 'X' or p1_choise != 'O':
        p1_choise = input(f"\n{p1_name}, Do you want to be X or O\t")[O].upper()
        if p1_choise == 'X' or p1_choise == 'O':
            break
        print("INVALID INPUT!")
    if p1_choise == 'X':
        p2_choise = 'O'
    elif p1_choise == 'O':
        p2_choise = 'X'
    return (p1_choise, p2_choise)
def first_player():
    import random
    return random.choice((0, 1))
def display_board(board, avail):
    print("   " + " {} | {} | {} ".format(board[7], board[8], board[9]) + "     " + " {} | {} | {} ".format(
        avail[7], avail[8], avail[9]))
    print("   " + "----------" + "         " + "----------")
    print("   " + " {} | {} | {} ".format(board[4], board[5], board[6]) + "     " + " {} | {} | {} ".format(
        avail[4], avail[5], avail[6]))
    print("   " + "----------" + "         " + "----------")
    print("   " + " {} | {} | {} ".format(board[1], board[2], board[3]) + "     " + " {} | {} | {} ".format(
        avail[1], avail[2], avail[3]))
def CompAI(board, name, choice):
    position = 0
    possibilities = [x for x, letter in enumerate(board) if letter == '' and x != 0]

    for let in ['O', 'X']:
        for i in possibilities:
            boardCopy = board[:]
            boardCopy[i] = let
            if (win_check(boardCopy, let)):
                position = i
                return position
    openCorners = [x for x in possibilities if x in [1, 3, 7, 9]]

    if len (openCorners) > 0:
        position = selectRandom(openCorners)
        return position

    if 5 in possibilities:
        position 5
        return position

    openEdges = [x for x in possibilities if x in [2, 4, 6, 8]]

    if len(openEdges) > 0:
        position = selectRandom(openEdges)
        return position

def selectRandom(board):
    import random
    ln = len(board)
    r = random.randrsnge(0, ln)
    return board[r]

def place_marker(board, avail, choice, position):
    board[position] = choice
    avail[position] = ''

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True
