# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(l):
    """
    for debugging
    """
    curr = l
    while curr is not None:
        print curr.val
        curr = curr.next

def getNextVal(lists):
    """
    given a list of linked lists, get next min
    value and update counter
    """
    res, index = 1e9, -1
    for i, l in enumerate(lists):
        if l is not None and l.val < res:
            res = l.val
            index = i
    if index != -1:
        lists[index] = lists[index].next
    return res


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nextVal = getNextVal(lists) 
        if nextVal == 1e9:
            return None
        res = ListNode(nextVal)

        curr = res
        nextVal = getNextVal(lists) 
        while nextVal != 1e9:
            curr.next = ListNode(nextVal)
            curr = curr.next
            nextVal = getNextVal(lists) 
        return res
