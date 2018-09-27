def cumsum(M):
    """
    substitute the value of M with their 2D cumsum in place,
    O(mn) time O(1) space
    """
    for i in xrange(1, len(M[0])):
        M[0][i] += M[0][i-1]
    for j in xrange(1, len(M)):
        M[j][0] += M[j-1][0]
    for j in xrange(1, len(M)):
        for i in xrange(1, len(M[0])):
            M[j][i] += M[j][i-1] + M[j-1][i] - M[j-1][i-1]

def getCumsum(e):
    return e & ((2 << 23)-1)

def getValue(e):
    return e >> 24

def setValue(e, value):
    return e + (value << 24)

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        this is a O(mn) time and O(1) solution
        - use bitwise operation to achieve O(1)
        - use cumsum optimization for time speed up
        """
        cumsum(M)
        for i in xrange(0, len(M[0])):
            for j in xrange(0, len(M)):
                x2 = min( i+1, len(M[0]) - 1)
                y2 = min( j+1, len(M) - 1)
                value = getCumsum(M[y2][x2]) 
                if (j-2)>=0:
                    value -= getCumsum(M[(j-2)][x2])
                if (i-2)>=0:
                    value -= getCumsum(M[y2][i-2])
                if (j-2)>=0 and (i-2)>=0:
                    value += getCumsum(M[j-2][i-2])
                area = ( x2 - max(0, i-1) + 1 ) * ( y2 - max(0, j-1) + 1 )
                M[j][i] = setValue( M[j][i], value/area )

        for i in xrange(0, len(M[0])):
            for j in xrange(0, len(M)):
                M[j][i] = getValue( M[j][i] )

        return M
           
        
