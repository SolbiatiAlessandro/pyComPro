class LinkedList():
    def __init__( self, n ):
        """
        self.next are the zero based next elem index
        self.prev are the zero based prev elem index
        """
        self.next   = [ i+1 for i in xrange(n-1) ] + [ int(1e9) ]
        self.prev   = [ int(-1e9) ] + [ i-1 for i in xrange(1,n) ]
        self.len    = n

    def checkPlace( self, place, target ):
        """
        given a place (1-based) and a target k (with the format specified in the task) return True is the condition in the task is met
        """
        #import pdb;pdb.set_trace() 
        if place > 1 and 0 <= place-1 < self.len and place - ( self.prev[ place - 1 ] +  1 ) == target + 1:
            return True
        if place < self.len and 0 <= place-1 < self.len and ( self.next[ place - 1 ] + 1 ) - place == target + 1:
            return True
        return False


    def removePlace( self, place ):
        """
        removes a 1-based place form the linked list
        """
        #import pdb;pdb.set_trace()
        if 0 <= place-1 < self.len:
            currNext = self.next[ place - 1 ]
            currPrev = self.prev[ place - 1 ]
            try:
                if place > 1:
                    self.next[ currPrev ] = currNext
                if place < self.len and currNext < self.len:
                    self.prev[ currNext ] = currPrev
            except TypeError:
                print "got a type error with {} {}".format( currNext, type(currNext) ) 


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """  
        lenFlowers = len( flowers )
        res, linkedList = -1, LinkedList( lenFlowers )
        for j in xrange( lenFlowers ):
            i = lenFlowers - j - 1
            if linkedList.checkPlace( flowers[i], k ):
                res = i+1
            linkedList.removePlace( flowers[i] )
        return res
        

        
