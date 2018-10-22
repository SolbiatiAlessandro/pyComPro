import unittest
import l399


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l399.Solution()
    
    def test_solution(self):
        #import pdb;pdb.set_trace()
        got = self.s.findStrobogrammatic(1)
        self.assertItemsEqual(got, ['0', '1', '8'])
        print got
        got = self.s.findStrobogrammatic(2)
        print got
        got = self.s.findStrobogrammatic(2)
        self.assertItemsEqual(got, ["11","69","88","96"])
        got = self.s.findStrobogrammatic(3)
        self.assertItemsEqual(got, ['101', '808', '609', '906', '111', '818', '619', '916', '181', '888', '689', '986'])
        print got
        got = self.s.findStrobogrammatic(4)
        self.assertItemsEqual(got, ['1111', '8118', '6119', '9116', '1881', '8888', '6889', '9886', '1001', '8008', '6009', '9006', '1691', '8698', '6699', '9696', '1961', '8968', '6969', '9966'])
        print got




if __name__ == "__main__":
    unittest.main()
