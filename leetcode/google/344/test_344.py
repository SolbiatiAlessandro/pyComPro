import unittest
import l334
from  l334 import TreeNode


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l334.Solution()
    
    def test_solution(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.right = TreeNode(3)

        #import pdb;pdb.set_trace() 
        got = self.s.inorderSuccessor(tree, TreeNode(1))
        self.assertEqual(got, tree)

        tree = TreeNode(5)
        tree.left = TreeNode(3)
        tree.right = TreeNode(6)
        tree.left.left = TreeNode(2)
        tree.left.right = TreeNode(4)
        tree.left.left.left = TreeNode(1)

        #import pdb;pdb.set_trace()
        got = self.s.inorderSuccessor(tree, TreeNode(6))
        self.assertEqual(got, None)

        tree = TreeNode(2)
        tree.right = TreeNode(3)

        #import pdb;pdb.set_trace() 
        got = self.s.inorderSuccessor(tree, tree)
        self.assertEqual(got, tree.right)

        tree = TreeNode(6)
        tree.left = TreeNode(2)
        tree.left.right = TreeNode(4)
        tree.left.right.left = TreeNode(3)

        #import pdb;pdb.set_trace()
        got = self.s.inorderSuccessor(tree, tree.left)
        self.assertEqual(got, tree.left.right.left)



if __name__ == "__main__":
    unittest.main()
