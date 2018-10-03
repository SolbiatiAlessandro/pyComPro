# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(l):
    """
    for debugging
    """
    print ""
    curr = l
    while curr is not None:
        print curr.val
        curr = curr.next


def mergeTwoList(l1, l2):
    """
    given two sorted lists l1 l2 return a
    sorted merged list
    """
    res = ListNode('*')
    curr = res
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1 is None:
        curr.next = l2
    elif l2 is None:
        curr.next = l1
    return res.next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = None
        for l in sorted(lists):
            res = mergeTwoList(res, l)
        return res
