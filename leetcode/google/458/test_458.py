import unittest
import l458

def convert(nums):
    print "\n\n"
    print nums
    for num in nums:
        res = ""
        for x in reversed(xrange(8)):
            res += str(bool(num & (1 << x)))
        print res.replace("True","1").replace("False","0")


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l458.Solution()

    def test_solution( self ):
        data = [197, 130, 1]
        convert(data)
        got = self.s.validUtf8(data)
        self.assertEqual(got, True)
        
        data = [235, 140, 4]
        convert(data)
        got = self.s.validUtf8(data)
        self.assertEqual(got, False)
        
        data = [145]
        convert(data)
        got = self.s.validUtf8(data)
        self.assertEqual(got, False)

if __name__ == "__main__":
    unittest.main()
