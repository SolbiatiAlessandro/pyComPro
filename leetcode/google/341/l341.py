def lsearch( l, value ):
    """
    search index of value in ordered list l, optimized as a binary search later
    """
    #import pdb;pdb.set_trace()
    if value < l[0][0]:
        return 0
    for k,(v,_) in enumerate(l[:-1]):
        if v <= value < l[k+1][0]:
            return k+1
    return len(l)

def query( l, end, value, key ):
    """
    rtype:int -> return the trapped water by this close on value key
    """
    #import pdb;pdb.set_trace()
    res, insert = 0, lsearch( l, value ) 
    ll = [(end,-1)]+l
    for index,(start, val) in enumerate(ll[1:insert+2]):
        res += (key - val)*(min(start,value)-ll[index][0])
    del( l[:insert] )
    return res

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #import pdb;pdb.set_trace()
        if height == []:
            return  0
        res, prev, l, end =  0, height[0], [], height[0]
        for k,v in enumerate( height[1:] ):
            if v<prev:
                l = [(prev,k)] + l
                end = v
            elif v>prev:
                if l != []:
                    res += query( l, end, v, k) 
                    end = v
            prev = v
            #print k,prev,res
        return res
                
