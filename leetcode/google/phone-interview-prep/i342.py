# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        val, index = 1e9, -1
        for i, node in enumerate(lists):
            if node and node.val < val:
                val = node.val
                index = i
        if index == -1: return None
        res = lists[index]
        lists[index] = lists[index].next
        curr = res
        while True:
            val, index = 1e9, -1
            for i, node in enumerate(lists):
                if node and node.val < val:
                    val = node.val
                    index = i
            if index == -1: break
            curr.next = lists[index]
            curr = curr.next
            lists[index] = lists[index].next
        return res
        
                
            
        