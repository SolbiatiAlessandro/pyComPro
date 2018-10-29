import unittest
import l361b


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l361b.Solution()

    #@unittest.skip("Wait")
    def test_solution( self ):

        test_input = [3,2,1,5,6,4] 
        k = 2
        output = 5
        self.assertEqual(self.s.findKthLargest(test_input, k), output)

        #import pdb;pdb.set_trace()
        test_input = [3,2,3,1,2,4,5,5,6] 
        k = 4
        output = 4
        self.assertEqual(self.s.findKthLargest(test_input, k), output)

        test_input = range(20)
        k = 6
        output = 14
        self.assertEqual(self.s.findKthLargest(test_input, k), output)

        test_input = range(20)
        k = 14
        output = 6
        self.assertEqual(self.s.findKthLargest(test_input, k), output)

        test_input = range(100)
        for i in range(1, 100):
            k = i
            output = 100 - i
            try:
                self.assertEqual(self.s.findKthLargest(test_input, k), output)
            except:
                import pdb;pdb.set_trace() 
                pass

        import math
        from random import random
        for i in xrange(1, 100):
            test_input = [int(math.floor(random() * 100)) for _ in xrange(101)]
            k = i
            output = sorted(test_input)[-i]
            res = self.s.findKthLargest(test_input, k)
            try:
                self.assertEqual(res, output)
            except:
                import pdb;pdb.set_trace() 
                pass


if __name__ == "__main__":
    unittest.main()
