import unittest
import l463
from l463 import TreeNode


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l463.Solution()
    
    def test_solution(self):
        tree = TreeNode(4)
        tree.right = TreeNode(5)
        tree.left = TreeNode(2)
        tree.left.right = TreeNode(3)
        tree.left.left = TreeNode(1)

        got = self.s.closestValue(tree, 3.712)
        self.assertEqual(got, 4)

        tree = TreeNode(4.96)
        tree.right = TreeNode(5)
        tree.left = TreeNode(2)
        tree.left.right = TreeNode(2.1)
        tree.left.left = TreeNode(1)

        got = self.s.closestValue(tree, 3.712)
        self.assertEqual(got, 4.96)

        tree = TreeNode(4)

        got = self.s.closestValue(tree, 3.712)
        self.assertEqual(got, 4)

if __name__ == "__main__":
    unittest.main()
