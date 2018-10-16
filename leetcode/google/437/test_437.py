import unittest
import l437
from l437 import TreeNode


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l437.Solution()
    
    def test_solution(self):
        tree = TreeNode(2)
        tree.right = TreeNode(3)
        tree.left = TreeNode(1)
        got = self.s.isValidBST(tree)
        self.assertEqual(got, True)

        tree = TreeNode(5)
        tree.right = TreeNode(4)
        tree.left = TreeNode(1)
        tree.right.right = TreeNode(6)
        tree.right.left = TreeNode(3)
        got = self.s.isValidBST(tree)
        self.assertEqual(got, False)

        tree = TreeNode(5)
        tree.right = TreeNode(7)
        tree.left = TreeNode(1)
        tree.right.right = TreeNode(8)
        tree.right.left = TreeNode(6)
        got = self.s.isValidBST(tree)
        self.assertEqual(got, True)

        tree = TreeNode(1)
        tree.left = TreeNode(1)
        got = self.s.isValidBST(tree)
        self.assertEqual(got, False)

        tree = TreeNode(0)
        tree.right = TreeNode(-1)
        got = self.s.isValidBST(tree)
        self.assertEqual(got, False)


        print "okk"


if __name__ == "__main__":
    unittest.main()
