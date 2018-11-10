import unittest
import l456


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l456.Solution()

    def test_solution( self ):
        matrix =  [[1,   2,   2,   3,   5],
                     [3,   2,   3,   4,   4]  ,
                     [2,   4,   5,   3,   1]  ,
                     [6,   7,   1,   4,   5]  ,
                     [5,   1,   1,   2,   4]]
        got = self.s.pacificAtlantic(matrix)
        self.assertItemsEqual(got, [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
        
        got = self.s.pacificAtlantic([])
        self.assertEqual(got, [])

if __name__ == "__main__":
    unittest.main()

