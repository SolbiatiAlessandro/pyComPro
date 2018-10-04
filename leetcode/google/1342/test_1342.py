import unittest
import l1342
from l1342 import Node

def printList(node):
    print "\n"+str(node.val)
    curr = node.next
    while curr != node:
        print curr.val
        curr = curr.next

class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l1342.Solution()

    def test_solution( self ):
        head = Node(3, None)
        head.next = Node(4, None)
        head.next.next = Node(1, None)
        head.next.next.next = head

        printList(head)
        got = self.s.insert(head, 2)
        printList(got)

        expected = [3,4,1,2]
        self.assertEqual(got.val, expected[0])
        curr, i = got.next, 1
        self.assertEqual(got.val, expected[0])
        while curr != got:
            self.assertEqual(curr.val, expected[i])
            i+=1
            curr = curr.next

        got = self.s.insert(None, 5)
        self.assertEqual(got.val, 5)
        self.assertEqual(got, got.next)

        got = self.s.insert(got, 6)
        self.assertEqual(got.val, 5)
        self.assertEqual(got.next.val, 6)
        self.assertEqual(got.next.next, got)

        got = self.s.insert(None, 5)
        got = self.s.insert(got, 4)
        self.assertEqual(got.val, 5)
        self.assertEqual(got.next.val, 4)
        self.assertEqual(got.next.next, got)

        head = Node(3, None)
        head.next = Node(3, None)
        head.next.next = Node(3, None)
        head.next.next.next = head

        printList(head)
        got = self.s.insert(head, 0)
        printList(got)

        head = Node(3, None)
        head.next = Node(5, None)
        head.next.next = Node(1, None)
        head.next.next.next = head

        printList(head)
        got = self.s.insert(head, 0)
        printList(got)

        print "ok" 

if __name__ == "__main__":
    unittest.main()

