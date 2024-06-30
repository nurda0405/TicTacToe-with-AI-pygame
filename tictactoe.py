"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None
count = 0

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX, countO = 0,0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1
    if countX == countO:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append([i,j])
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    c = copy.deepcopy(board)
    c[action[0]][action[1]] = player(board)
    return c


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        count_horizontal = 0
        count_vertical = 0

        for j in range(3):
            if board[i][j] == X:
                count_horizontal += 1
            elif board[i][j] == O:
                count_horizontal -= 1
            if board[j][i] == X:
                count_vertical += 1
            elif board[j][i] == O:
                count_vertical -= 1
        if count_horizontal == 3 or count_vertical == 3:
            return X
        elif count_horizontal == -3 or count_vertical == -3:
            return O
        
    count_diagonal1 = 0
    count_diagonal2 = 0
    for i in range(3):
        if board[2-i][i] == X:
            count_diagonal2 += 1
        elif board[2-i][i] == O:
            count_diagonal2 -= 1
        if board[i][i] == X:
            count_diagonal1 += 1
        elif board[i][i] == O:
            count_diagonal1 -= 1
    if count_diagonal1 == 3 or count_diagonal2 == 3:
        return X
    elif count_diagonal1 == -3 or count_diagonal2 == -3:
        return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """



def minimax(board, level):
    global count
    """
    Returns the optimal action for the current player on the board.
    """
    count += 1
    print(count)
    if terminal(board):
        w = winner(board)
        print(count)
        '''
        for i in range(3):
            print(board[i])
        '''
        if w == X:
            return 1
        elif w == O:
            return -1
        else:
            return 0
        
    else:
        print(count)
        point = 0
        move = []
        if player(board) == X:
            point = -10
            for action in actions(board):
                res = minimax(result(board, action), level + 1)
                if res > point:
                    move = action
                    point = res
                if point == 1:
                    if level == 1:
                        return action
                    else:
                        return 1
        else:
            point = 10
            for action in actions(board):
                res = minimax(result(board, action), level + 1)
                if res < point:
                    move = action
                    point = res
                if point == -1:
                    if level == 1:
                        return action
                    else:
                        return -1
        if level == 1:
            return move
        else:
            return point
        
            #play for both players in intellegent way, and choose the efficient turn 

for i in range(3):
    print([[None,O,X],
               [None,X,None],
               [O,None,X]][i])
print('\n')
print(minimax([[O,None,None],
               [None,X,None],
               [None,O,X]], 1))
