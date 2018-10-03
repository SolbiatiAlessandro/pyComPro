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

def getNextNode(lists):
    """
    given a list of linked lists, get next min node
    and update counter
    """
    nodeRes, res, index = None, 1e9, -1
    for i, l in enumerate(lists):
        if l is not None and l.val < res:
            res = l.val
            nodeRes = l
            index = i
    if index != -1:
        lists[index] = lists[index].next
    return nodeRes


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nextVal = getNextNode(lists) 
        res = nextVal

        curr = nextVal
        nextVal = getNextNode(lists) 
        while nextVal != None:
            curr.next = nextVal
            curr = curr.next
            nextVal = getNextNode(lists) 
        return res
