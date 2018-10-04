class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        #import pdb;pdb.set_trace()
        res = head
        if res is None:
            res = Node(insertVal, None)
            res.next = res
            return res

        if res.next == res:
            res.next = Node(insertVal, res)
            return res

        curr = head
        while True:
            if curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    curr.next = Node(insertVal, curr.next)
                    return res
            if curr.val <= insertVal < curr.next.val:
                curr.next = Node(insertVal, curr.next)
                return res
            if curr.next == head:
                curr.next = Node(insertVal, curr.next)
                return res
            curr = curr.next

