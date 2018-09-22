def lsearch( l, value ):
    """
    search index of value in ordered list l, optimized as a binary search 
    """
    if value < l[0][0]:
        return 0
    if value >= l[len(l)-1][0]:
        return len(l)

    a,b=0,len(l)-1
    while a<=b:
        m=(b-a)/2+a
        if l[m][0]<=value<l[m+1][0]:
            return m+1
        elif value < l[m][0]:
            b=m-1
        else:
            a=m+1

def query( l, end, value, key ):
    """
    rtype:int -> return the trapped water by this close on value key
    """
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
        return res
                
