import unittest
import l442


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l442.Solution()

    def test_bitwise( self ):

        a = 50
        b = 100
        a = l442.setValue( a, b ) 
        self.assertEqual( l442.getCumsum(a), 50 )
        self.assertEqual( l442.getValue(a), 100 )

        a = 150*150*255
        b = 255
        a = l442.setValue( a, b ) 
        self.assertEqual( l442.getCumsum(a), 150*150*255 )
        self.assertEqual( l442.getValue(a), 255 )


    def test_cumsum( self ):

        M = [[1,1,1],[1,1,1],[1,1,1]]
        l442.cumsum(M)
        expected = [[1,2,3],[2,4,6],[3,6,9]]
        self.assertEqual( M, expected )


    def test_solution( self ):

        M = [[1,1,1],
         [1,0,1],
         [1,1,1]]
        expected = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
        got = self.s.imageSmoother( M )
        self.assertEqual( got, expected )

        M = [[1,1,1],
         [1,1,1],
         [1,1,1]]
        expected = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]
        got = self.s.imageSmoother( M )
        self.assertEqual( got, expected )

        M = [[1,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [1,1,1,1]]
        expected = [[1,1, 1, 1],
         [1, 1, 1,1],
         [1, 1, 1,1],
         [1, 1,1, 1]]
        got = self.s.imageSmoother( M )
        self.assertEqual( got, expected )
        
        M = [[1,1],
         [1,1]]
        expected = [[1, 1],
         [1, 1]]
        got = self.s.imageSmoother( M )
        self.assertEqual( got, expected )

        M = [[1]]
        expected = [[1]]
        got = self.s.imageSmoother( M )
        self.assertEqual( got, expected )

        M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
        expected = [[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]]
        got = self.s.imageSmoother( M )
        self.assertEqual( got, expected )

        print "ok"


if __name__ == "__main__":
    unittest.main()

