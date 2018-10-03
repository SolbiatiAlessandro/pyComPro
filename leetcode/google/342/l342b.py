class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getLists(lists):
    """
    return a list of python lists
    """
    res, index, maxLen = [], -1, -1
    for i, l in enumerate(lists):
        newList = []
        while l is not None:
            newList.append(l.val)
            l = l.next
        if len(newList) > maxLen:
            maxLen = len(newList)
            index = i
        res.append(newList)
    return res, index


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists, index = getLists(lists)
        if len(lists) == 0 or len(lists[index]) == 0:
            return None
        res = lists[index]
        for i, l in enumerate(lists):
            if i != index:
                lCnt, resCnt = 0, 0
                while lCnt < len(l) and resCnt < len(res):
                    if l[lCnt] < res[resCnt]:
                        res.insert(resCnt, l[lCnt])
                        lCnt+=1
                    resCnt+=1
                while lCnt < len(l):
                    res.append(l[lCnt])
                    lCnt+=1
        resList = ListNode(res[0])
        curr = resList
        for i in xrange(1,len(res)):
            curr.next = ListNode(res[i])
            curr = curr.next
        return resList



