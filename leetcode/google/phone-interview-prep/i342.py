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
        from Queue import PriorityQueue
        q = PriorityQueue()
        for i, node in enumerate(lists):
            if node: q.put((node.val,i))
        nums = []
        while not q.empty():
            val, index = q.get()
            lists[index] = lists[index].next
            nums.append(val)
            if lists[index]: q.put((lists[index].val, index))
            
        if not nums: return None
        res = ListNode(nums[0])
        curr = res
        for num in nums[1:]:
            curr.next = ListNode(num)
            curr = curr.next
        return res