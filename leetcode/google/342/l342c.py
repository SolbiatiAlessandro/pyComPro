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
        helper = {}
        for l in lists:
            while l is not None:
                if helper.get(l.val) is None:
                    helper[l.val] = 1
                else:
                    helper[l.val] += 1
                l = l.next
        res = ListNode(0)
        curr = res
        for k, v in sorted(helper.items()):
            for i in xrange(v):
                curr.next = ListNode(k)
                curr = curr.next
        return res.next

            
            

