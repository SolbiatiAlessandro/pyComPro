import unittest
import l470

class testBinaryTree( unittest.TestCase ):

    def test_insert( self ):
        tree = l470.Node(2)
        u,l = tree.insert( 4 )
        self.assertEqual( u, 1e9 )
        self.assertEqual( l, 2 )
        u,l = tree.insert( 1 )
        self.assertEqual( u, 2 )
        self.assertEqual( l, 0 )
        u,l = tree.insert( 5 )
        self.assertEqual( u, 1e9 )
        self.assertEqual( l, 4 )
        u,l = tree.insert( 3 )
        self.assertEqual( u, 4 )
        self.assertEqual( l, 2 )
        
        self.assertTrue( tree.value == 2 )
        self.assertTrue( tree.right.value == 4 )
        self.assertTrue( tree.left.value == 1 )
        self.assertTrue( tree.right.right.value == 5 )
        self.assertTrue( tree.right.left.value == 3 )
        

class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l470.Solution()

    def test_example( self ):

        flowers = [1,3,2]
        k = 1
        got = self.s.kEmptySlots( flowers, k )
        self.assertEqual( got, 2 )

        flowers = [1,2,3]
        got = self.s.kEmptySlots( flowers, k )
        self.assertEqual( got, -1 )

        flowers = [1,3,7,9,5,6]
        got = self.s.kEmptySlots( flowers, 3 )
        self.assertEqual( got, 3 )
        got = self.s.kEmptySlots( flowers, 2 )
        self.assertEqual( got, -1 )
        got = self.s.kEmptySlots( flowers, 1 )
        self.assertEqual( got, 2 )
        got = self.s.kEmptySlots( flowers, 0 )
        self.assertEqual( got, 6 )

        
        got = self.s.kEmptySlots( [], 0 )
        self.assertEqual( got, -1 )

        got = self.s.kEmptySlots( [1], 0 )
        self.assertEqual( got, -1 )

        got = self.s.kEmptySlots( [1,2], 0 )
        self.assertEqual( got, 2 )

if __name__ == "__main__":
    unittest.main()
