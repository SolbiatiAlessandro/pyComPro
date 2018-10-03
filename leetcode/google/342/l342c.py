# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dt, res = {}, ListNode(0)
        for l in lists:
            while l is not None:
                dt[l.val] = 1 if dt.get(l.val) is None else dt[l.val]+1
                l = l.next
        curr = res
        for k, v in sorted(dt.items()):
            for i in xrange(v):
                curr.next = ListNode(k)
                curr = curr.next
        return res.next

            
            

