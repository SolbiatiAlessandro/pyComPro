class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        q = PriorityQueue()
        for i, l in enumerate(lists):
            if l:
                q.put((l.val, i))

        try: got = q.get_nowait()
        except: return None
        res = ListNode(got[0])
        lists[got[1]] = lists[got[1]].next
        if lists[got[1]]: q.put((lists[got[1]].val, got[1]))
        curr = res

        while True:
            try: got = q.get_nowait()
            except: return res
            curr.next = ListNode(got[0])
            lists[got[1]] = lists[got[1]].next
            curr = curr.next
            if lists[got[1]]: q.put((lists[got[1]].val, got[1]))



if __name__ == "__main__":
    # 1->4->5
    # 1->3->4
    # 2->6
    l1,l2,l3 = ListNode(1), ListNode(1), ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3.next = ListNode(6)
    lists = [l1,l2,l3]
    s = Solution()
    got, i= s.mergeKLists(lists), 0
    expected = [1,1,2,3,4,4,5]
    assert got
    while got and i < len(expected):
        assert got.val == expected[i]
        i += 1
        got = got.next
