import unittest
import l338


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l338.Solution()

    def test_solution( self ):
        
        matrix = [
                     [ 1, 2, 3 ],
                     [ 4, 5, 6 ],
                     [ 7, 8, 9 ]
                    ]
        got = self.s.spiralOrder( matrix )
        self.assertEqual( got, [1,2,3,6,9,8,7,4,5] )

        matrix = [
                      [1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9,10,11,12]
                    ]
        got = self.s.spiralOrder( matrix )
        self.assertEqual( got, [1,2,3,4,8,12,11,10,9,5,6,7] )

        matrix = [[0]]
        got = self.s.spiralOrder( matrix )
        self.assertEqual( got, [0] )

        matrix = [[0],[1],[2]]
        got = self.s.spiralOrder( matrix )
        self.assertEqual( got, [0,1,2] )


        

if __name__ == "__main__":
    unittest.main()

