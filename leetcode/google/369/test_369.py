import unittest
import l369b


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l369b.Solution()

    def test_solution(self):
        #import pdb;pdb.set_trace() 
        test_input, prer = 2, [[1, 0]]
        test_output = True
        got = self.s.canFinish(test_input, prer)
        self.assertEqual(got, test_output)

        test_input, prer = 2, [[1, 0], [0, 1]]
        test_output = False
        #import pdb;pdb.set_trace()
        got = self.s.canFinish(test_input, prer)
        self.assertEqual(got, test_output)

        #import pdb;pdb.set_trace()
        test_input, prer = 3, [[1, 0], [0, 2], [2, 1]]
        test_output = False
        got = self.s.canFinish(test_input, prer)
        self.assertEqual(got, test_output)


if __name__ == "__main__":
    unittest.main()
