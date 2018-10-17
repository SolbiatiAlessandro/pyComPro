import unittest
import l370


class testSolution(unittest.TestCase):

    def setUp(self):
        self.s = l370.Solution()
    
    def test_is_valid(self):
        l370.WORDS = ["area","lead","wall","lady","ball"]
        l370.LEN = 4
        l370.N = 5
        got = l370.is_valid([3,1,0])
        self.assertEqual(got, True)
        got = l370.is_valid([3,2,0])
        self.assertEqual(got, False)
        got = l370.is_valid([3,1,0,4])
        self.assertEqual(got, True)
        got = l370.is_valid([3,1,0,2])
        self.assertEqual(got, True)
        got = l370.is_valid([3,1,2,4])
        self.assertEqual(got, False)
        got = l370.is_valid([3,1])
        self.assertEqual(got, True)
        got = l370.is_valid([3])
        self.assertEqual(got, True)

    def test_solve(self):
        l370.WORDS = ["area","lead","wall","lady","ball"]
        l370.LEN = 4
        l370.N = 5
        l370.RES = []
        l370.solve([3,1,0,4])
        self.assertEqual(l370.RES, [[3,1,0,4]])
        #import pdb;pdb.set_trace()
        l370.RES = []
        got = l370.solve([3,1,0])
        self.assertListEqual(sorted(l370.RES), sorted([[3,1,0,4],[3,1,0,2]]))


    #@unittest.skip("wait")
    def test_solution(self):
        words = ["area","lead","wall","lady","ball"]
        expected = [
          [ "wall",
            "area",
            "lead",
            "lady"
          ],
          [ "ball",
            "area",
            "lead",
            "lady"
          ]
        ]
        got = self.s.wordSquares(words)
        self.assertItemsEqual(got, expected)
        import pdb;pdb.set_trace()
        words = ["abat","baba","atan","atal"]
        expected = [
          [ "baba",
            "abat",
            "baba",
            "atan"
          ],
          [ "baba",
            "abat",
            "baba",
            "atal"
          ]
        ]
        got = self.s.wordSquares(words)
        self.assertItemsEqual(got, expected)


if __name__ == "__main__":
    unittest.main()
