import unittest
import l342
from l342 import ListNode


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l342.Solution()

    @unittest.skip("wait")
    def test_nextval(self):
        
        l1 = ListNode(1)
        l1.next = ListNode(4)
        l1.next.next = ListNode(5)

        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(5)

        l3 = ListNode(2)
        l3.next = ListNode(6)

        expected = ListNode(1)
        curr = expected
        curr.next = ListNode(1)
        curr = curr.next
        curr.next = ListNode(2)
        curr = curr.next
        curr.next = ListNode(3)
        curr = curr.next
        curr.next = ListNode(4)
        curr = curr.next
        curr.next = ListNode(4)
        curr = curr.next
        curr.next = ListNode(5)
        curr = curr.next
        curr.next = ListNode(6)
        curr = curr.next

        lists = [l1,l2,l3]

        got = l342.getNextVal(lists)
        self.assertEqual(got,1)

        got = l342.getNextVal(lists)
        self.assertEqual(got,1)

        got = l342.getNextVal(lists)
        self.assertEqual(got,2)


    #@unittest.skip("Wait")
    def test_solution( self ):
        l1 = ListNode(1)
        l1.next = ListNode(4)
        l1.next.next = ListNode(5)

        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(5)

        l3 = ListNode(2)
        l3.next = ListNode(6)

        expected = ListNode(1)
        curr = expected
        curr.next = ListNode(1)
        curr = curr.next
        curr.next = ListNode(2)
        curr = curr.next
        curr.next = ListNode(3)
        curr = curr.next
        curr.next = ListNode(4)
        curr = curr.next
        curr.next = ListNode(5)
        curr = curr.next
        curr.next = ListNode(5)
        curr = curr.next
        curr.next = ListNode(6)
        curr = curr.next

        got = self.s.mergeKLists( [l1,l2,l3] )
        curr1, curr2 = got, expected
        while curr1 is not None and curr2 is not None:
            self.assertEqual( curr1.val, curr2.val )
            curr1 = curr1.next
            curr2 = curr2.next

        got = self.s.mergeKLists( [] )
        self.assertEqual(got, None)

        l1 = ListNode(1)
        l1.next = ListNode(4)
        l1.next.next = ListNode(5)
        got = self.s.mergeKLists( [l1] )
        l342.printList(got)

        

if __name__ == "__main__":
    unittest.main()

