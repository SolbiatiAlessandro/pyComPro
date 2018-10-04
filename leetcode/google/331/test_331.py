import unittest
import l331


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l331.Solution()

    def test_solution( self ):
        equations = [ ["a", "b"], ["b", "c"] ]
        values = [2.0, 3.0]
        queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
        got = self.s.calcEquation(equations, values, queries)
        self.assertEqual(got, [6.0, 0.5, -1.0, 1.0, -1.0 ])
        
        equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
        values = [3.0,4.0,5.0,6.0]
        queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]

        #import pdb;pdb.set_trace()
        got = self.s.calcEquation(equations, values, queries)
        self.assertEqual(got, [360.0,0.00833,20.0,1.0,-1.0,-1.0])


        

if __name__ == "__main__":
    unittest.main()

