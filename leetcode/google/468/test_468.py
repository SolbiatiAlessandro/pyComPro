import unittest
import l468


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l468.Solution()

    def test_solution( self ):
        got = self.s.evalRPN(["2", "1", "+", "3", "*"])
        self.assertEqual(got, 9 )

        got = self.s.evalRPN(["4", "13", "5", "/", "+"])
        self.assertEqual(got, 6)

        got = self.s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        self.assertEqual(got, 22)
        

if __name__ == "__main__":
    unittest.main()

