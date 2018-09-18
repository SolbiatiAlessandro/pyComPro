class Node():
    def __init__( self, x ):
        self.value = x
        self.left = None
        self.right = None

    def insert( self, x ):
        ub, lb = 1e9, 0
        if x > self.value:
            if self.right is None:
                self.right = Node( x )
                return ub, self.value
            else:
                ub, lb = self.right.insert( x )
                if self.value > lb:
                    lb = self.value
        else:
            if self.left is None:
                self.left = Node( x )
                return self.value, lb
            else:
                ub, lb = self.left.insert( x )
                if self.value < ub:
                    ub = self.value

        return ub, lb


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """  
        tree = Node( flowers[0] ) if len( flowers ) > 0 else None
        for day in xrange(1,len(flowers)):
            flower = flowers[ day ]
            right, left = tree.insert( flower )
            if right != 1e9 and right - flower - 1 == k:
                return day+1
            if left !=0 and flower - left - 1 == k:
                return day+1
        return -1


