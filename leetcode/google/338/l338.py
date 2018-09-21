class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        i,j,res = 0,0,[]
        while matrix !=  []:
            m, n = len(matrix), len(matrix[0])
            if i == 0 and j == 0:
                res+=matrix[0]
                del( matrix[0] )
                i = n-1
            elif i == n-1 and j == 0:
                for j in xrange(0,m):
                    res+=[matrix[j][n-1]]
                    del( matrix[j][n-1] )
                i -= 1
            elif i == n-1 and j == m-1:
                res+=matrix[m-1][::-1]
                del( matrix[m-1] )
                j -= 1
                i = 0
            elif i == 0 and j == m-1:
                for j in reversed(xrange(0,m)):
                    res+=[matrix[j][0]]
                    del( matrix[j][0] )
        return res

            
