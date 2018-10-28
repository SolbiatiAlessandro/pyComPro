import unittest
import l345b


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l345b.Solution()

    def test_solution( self ):
        #import pdb;pdb.set_trace() 
        S, T = "ADOBECODEBANC", "ABC"
        expected = "BANC"
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)

        S, T = "A", "AA"
        expected = ""
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)

        S, T = "ADOBECODEBANC", "AKBC"
        expected = ""
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)

        S, T = "ADOBECODEBANC", "CODE"
        expected = "ECOD"
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)

        S, T = "ADOBECODEBANC", "BO"
        expected = "OB"
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)

        S, T = "ADOBECODEBANC", "CD"
        expected = "COD"
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)

        S, T = "ADOBECODEBANC", "DDCD"
        expected = ""
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)
        

        S, T = "ADOBECODEBANC", "ADOBECODEBANC"
        expected = "ADOBECODEBANC"
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)

        S, T = "BAAECABAECB", "BBCE"
        expected = "BAECB"
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)

        S, T = "B", "A"
        expected = ""
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)

        S, T = "BBA", "AB"
        expected = "BA"
        got = self.s.minWindow(S,T)
        self.assertEqual(got, expected)



        
if __name__ == "__main__":
    unittest.main()

