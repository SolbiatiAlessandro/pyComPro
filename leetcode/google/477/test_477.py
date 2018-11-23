import unittest
import l477


class testSolution(unittest.TestCase):
    
    def test_solution( self ):
        
        matrix = [
                  [3, 0, 1, 4, 2],
                  [5, 6, 3, 2, 1],
                  [1, 2, 0, 1, 5],
                  [4, 1, 0, 1, 7],
                  [1, 0, 3, 0, 5]
                ]

        m = l477.NumMatrix(matrix)
        got = m.sumRegion(2, 1, 4, 3) 
        self.assertEqual(got, 8)
        m.update(3, 2, 2)
        got = m.sumRegion(2, 1, 4, 3)
        self.assertEqual(got, 10)


if __name__ == "__main__":
    unittest.main()
