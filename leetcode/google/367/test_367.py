import unittest
import l367


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l367.Solution()

    def test_solution( self ):
        flights = [[0,1,1],[1,0,1],[1,1,0]]
        days = [[1,3,1],[6,0,3],[3,3,3]]
        got = self.s.maxVacationDays(flights, days)
        self.assertEqual(got, 12)
       
        flights = [[0,0,0],[0,0,0],[0,0,0]]
        days = [[1,1,1],[7,7,7],[7,7,7]]
        got = self.s.maxVacationDays(flights, days)
        self.assertEqual(got, 3)

        flights = [[0,1,1],[1,0,1],[1,1,0]]
        days = [[7,0,0],[0,7,0],[0,0,7]]
        got = self.s.maxVacationDays(flights, days)
        self.assertEqual(got, 21)

if __name__ == "__main__":
    unittest.main()

