board = {}
def initialize(n):
    for key in ['queen', 'row', 'col', 'nwtose', 'swtone']:
        board[key] = {}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(-(n-1), n):
        board['nwtose'][i] = 0
    for i in range(2*n - 1):
        board['swtone'][i] = 0

def printboard():
    for row in sorted(board['queen'].keys()):
        print(row, board['queen'][row])

def free(i, j):
    return board