import unittest
import B3


class testSolution(unittest.TestCase):

    def test_solution( self ):
        solve = B3.solve
        self.assertEqual(solve("GGGSGGGSGG"), 7)
        self.assertEqual(solve("GGGGGGGG"), 8)
        self.assertEqual(solve("SSSSSSSS"), 0)
        self.assertEqual(solve("GGGGGGSSSSSS"), 6)
        self.assertEqual(solve("SSSSSSGGG"), 3)
        self.assertEqual(solve("GGSSGGSSGG"), 3)
        self.assertEqual(solve("GSGSGSG"), 3)
        self.assertEqual(solve("GGGGGGGGGGS"), 10)
        self.assertEqual(solve("SGGGGGS"), 5)
        print "okk"
        

if __name__ == "__main__":
    unittest.main()

