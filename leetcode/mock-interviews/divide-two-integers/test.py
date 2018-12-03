import unittest
import divide


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = divide.Solution()

    def test_solution( self ):
        
        got = self.s.divide(10, 3)
        self.assertEqual(got, 3)
        got = self.s.divide(91, 5)
        self.assertEqual(got, 91/5)
        import pdb;pdb.set_trace() 
        got = self.s.divide(126, 21)
        self.assertEqual(got, 6)

        from random import random
        for _ in xrange(100):
            a = int(random()*1000)
            b = int(random()*1000)
            got = self.s.divide(b, a)
            print got, b, a
            self.assertEqual(got, b/a)
        

if __name__ == "__main__":
    unittest.main()

