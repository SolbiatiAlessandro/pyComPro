def update( cnt, cell ):
    """
    return the updated value of cell based on cnt
    :rtype int in [-1,0,1,2]

    update is the logic to compute the dummy value
    """
    if cell == 1:
        if cnt < 2 or cnt > 3:
            return -1
        return 1
    if cell == 0:
        if cnt == 3:
            return 2
        return 0

def cnt( board, x, y ):
    """
    :board, input board
    :x,y (int) where is the cell to execute cnt on

    the cnt function iterate over the (max) 8 cells surrounding x,y
    and overwrite the contents with the new dummy value
    """
    res = 0
    for i in xrange(-1+x,2+x):
        if 0 <= i < len(board[0]):
            for j in xrange(-1+y,2+y):
                if 0 <= j < len(board):
                   if not ( i == x and j == y ) and board[j][i] == 1 or board[j][i] == -1:
                        res+=1
    return res


def cleanBoard( board ):
    """
    replace dummy values with real values
    """
    for x in xrange(len(board[0])):
        for y in xrange(len(board)):
            if board[y][x] == 2:
                board[y][x] = 1
            elif board[y][x] == -1:
                board[y][x] = 0


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.

        the solution is in-place an achieve O(1) memory using a dummy value trick:
        i am updating the next state of a cell using the following table

          value | current state | next state |
            0           0             0
            1           1             1
            2           0             1
            -1          1             0

        with this trick you can overwrite in place without the need of additional memory,
        and when you look back at the cell later you know what was the previous state
        """
        #import pdb;pdb.set_trace()
        for x in xrange(len(board[0])):
            for y in xrange(len(board)):
                newCount = cnt( board, x, y) # this is counting the live cells surrounding x,y
                board[y][x] = update( newCount, board[y][x] ) # this overwrites the board in place
        cleanBoard( board ) # this clear the board from dummy values
       
        
        
