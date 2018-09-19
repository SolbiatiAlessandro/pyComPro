import unittest
import l473

class testTraverse( unittest.TestCase ):

    def setUp( self ):

        self.root = l473.TreeNode( 3 )
        self.root.left = l473.TreeNode( 4 )
        self.root.left.left = l473.TreeNode( 4 )
        self.root.left.right = l473.TreeNode( 4 )
        self.root.right = l473.TreeNode( 5 )
        self.root.right.right = l473.TreeNode( 5 )

    def test_assignDepth( self ):

        l473.assignDepth( self.root, -1, -1 )

        self.assertEqual( self.root.depth, 0 )
        self.assertEqual( self.root.right.right.depth , 1 )
        self.assertEqual( self.root.right.depth , 0 )
        self.assertEqual( self.root.left.right.depth , 1 )
        self.assertEqual( self.root.left.left.depth , 1 )
        self.assertEqual( self.root.left.depth , 0 )

    def test_computeMax( self ):

        res = 0
        l473.assignDepth( self.root, -1, -1 )
        res = l473.computeMax( self.root, res )
        self.assertEqual( res, 2 )

    def test_solution( self ):

        self.assertEqual( l473.Solution().longestUnivaluePath( self.root ), 2 )

if __name__ == "__main__":
    unittest.main()
