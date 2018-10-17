import unittest
import l370b


class testSolution(unittest.TestCase):

    def setUp(self):
        self.s = l370b.Solution()

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
        #import pdb;pdb.set_trace()
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
