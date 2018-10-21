import unittest
import l370e


class testSolution(unittest.TestCase):

    def setUp(self):
        self.s = l370e.Solution()
        self.words = ["area","lead","wall","lady","ball"]
        self.s.words = ["area","lead","wall","lady","ball"]

    #@unittest.skip("wait")
    def test_get_matches(self):
        gm = l370e.get_matches
        words = l370e.build_table(self.words)
        got = gm(words, "b")
        self.assertItemsEqual(got, [4])
        got = gm(words, "l")
        self.assertItemsEqual(got, [1,3])
        got = gm(words, "r")
        self.assertFalse(got)
        got = gm(words, "lk")
        self.assertFalse(got)
        got = gm(words, "rk")
        self.assertFalse(got)

        raw = ["abbba", "abbbc", "abbbd", "abbaa", "abbka", "abbia", "abjaa"]
        words = l370e.build_table(raw)
        got = gm(words, "a")
        self.assertItemsEqual(got, range(len(raw)))
        got = gm(words, "ab")
        self.assertItemsEqual(got, range(len(raw)))
        got = gm(words, "abb")
        self.assertItemsEqual(got, range(len(raw)-1))
        got = gm(words, "abbb")
        self.assertItemsEqual(got, range(3))

    
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
