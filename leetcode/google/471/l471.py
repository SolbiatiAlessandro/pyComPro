def timeDifference( A, B ):
    """
    :type A: str, first time for the subtraction B-A
    :type B: str, second time for the subtraction B-A
    :rtype int, difference between to times in minutes
    """
    #print("timeDifference called with {}".format(B))
    hourA, minA = int(A[:2]), int(A[3:])
    hourB, minB = int(B[:2]), int(B[3:])

    # import pdb;pdb.set_trace()
    minRes, r = minB - minA, 0
    if minRes < 0:
        minRes += 60 
        r = 1
    hourRes = hourB - hourA - r
    if hourRes < 0:
        hourRes += 24
    res = minRes + 60*hourRes
    return res if res > 0 else 24*60 
    
        
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        #import pdb;pdb.set_trace() 
        numbers = set([int(time[0]), int(time[1]), int(time[3]), int(time[4])]) 
        minimumDifference, res = 1e9, ""
        for h1 in numbers:
            if h1 <= 2:
                for h2 in numbers:
                    if h1 != 2 or ( h1 == 2 and h2 < 4 ):
                        for m1 in numbers:
                            if m1 <= 5:
                                for m2 in numbers:
                                    newTime = str(h1)+str(h2)+':'+str(m1)+str(m2)
                                    newDifference = timeDifference( time, newTime)
                                    if newDifference < minimumDifference :
                                        minimumDifference = newDifference
                                        res = newTime
        return res



