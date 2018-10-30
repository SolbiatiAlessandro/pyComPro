import unittest
import l364


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l364.Solution()

    def test_solution( self ):
        grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
        got = self.s.shortestDistance(grid)
        self.assertEqual(got, 7)

        grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0],[0,1,0,0,0]]
        got = self.s.shortestDistance(grid)
        self.assertEqual(got, 10)

    #@unittest.skip("wait")
    def test_optimization(self):
        from time import time
        grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,2,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        t = time()
        got = self.s.shortestDistance(grid)
        t1 = time()
        self.assertEqual(got, 7)
        print t1 - t

    #@unittest.skip("wait")
    def test_custom(self):
        grid = [[1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,1],[1,1,1,1,1,1,0,1],[1,0,0,0,0,1,0,1],[1,0,1,1,0,1,0,1],[1,0,1,0,0,1,0,1],[1,0,1,1,1,1,0,1],[1,0,0,0,0,0,0,1],[0,1,1,1,1,1,1,0]]
        from time import time
        t = time()
        got = self.s.shortestDistance(grid)
        t1 = time()
        print t1-t
        self.assertEqual(got, 269)

    def test_connected_comp(self):
        grid = [[1,0]]
        got = self.s.shortestDistance(grid)
        self.assertEqual(got, 1)

        

if __name__ == "__main__":
    unittest.main()

