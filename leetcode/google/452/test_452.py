import unittest
import l452b


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l452b.Solution()

    #@unittest.skip("")
    def test_solution( self ):
        matrix = [
                 [ 1, 2, 3 ],
                 [ 4, 5, 6 ],
                 [ 7, 8, 9 ]
                ]
        got = self.s.findDiagonalOrder(matrix)
        self.assertEqual(got , [1,2,4,7,5,3,6,8,9])
                        
        matrix = [
                 [ 1, 2 ],
                 [ 4, 5 ]
                ]
        got = self.s.findDiagonalOrder(matrix)
        self.assertEqual(got , [1,2,4,5])
                        
        matrix = [
                 [ 1 ]
                ]
        got = self.s.findDiagonalOrder(matrix)
        self.assertEqual(got , [1])

        matrix = []
        got = self.s.findDiagonalOrder(matrix)
        self.assertEqual(got , [])

    def test_notsquare(self):
        matrix = [
                 [ 1, 2, 3, 4 ],
                 [ 5, 6, 7, 8 ]
                ]
        got = self.s.findDiagonalOrder(matrix)
        self.assertEqual(got , [1,2,5,6,3,4,7,8])

        matrix = [
                 [ 1, 2, 3, 4 ],
                ]
        got = self.s.findDiagonalOrder(matrix)
        self.assertEqual(got , [1,2,3,4])

        matrix = [
                 [ 1 ],
                 [ 2 ],
                 [ 3 ],
                 [ 4 ],
                ]
        got = self.s.findDiagonalOrder(matrix)
        self.assertEqual(got , [1,2,3,4])


                        


if __name__ == "__main__":
    unittest.main()

