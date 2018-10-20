import unittest
import l370c


class testSolution(unittest.TestCase):

    def setUp(self):
        self.s = l370c.Solution()
        self.s.words = ["area","lead","wall","lady","ball"]


    def test_binary_search(self):
        bs = l370c.binary_search
        #import pdb;pdb.set_trace()
        words = sorted(zip(self.s.words, xrange(len(self.s.words))))
        got = bs(words, "wa")
        self.assertEqual(got[0], 2)
        got = bs(words, "ar")
        self.assertEqual(got[0], 0)
        got = bs(words, "le")
        self.assertEqual(got[0], 1)
        got = bs(words, "lad")
        self.assertEqual(got[0], 3)
        got = bs(words, "b")
        self.assertEqual(got[0], 4)
        got = bs(words, "k")
        self.assertEqual(got[0], -1)
        got = bs(words, "aaaa")
        self.assertEqual(got[0], -1)
        got = bs(words, "zzzz")
        self.assertEqual(got[0], -1)

    def test_get_matches(self):
        gm = l370c.get_matches
        words = sorted(zip(self.s.words, xrange(len(self.s.words))))
        got = gm(words, "b")
        self.assertItemsEqual(got, [4])
        got = gm(words, "l")
        self.assertItemsEqual(got, [1,3])

        raw = ["abbba", "abbbc", "abbbd", "abba", "abbk", "abbi", "abj"]
        words = sorted(zip(raw, xrange(len(raw))))
        got = gm(words, "a")
        self.assertItemsEqual(got, range(len(raw)))
        got = gm(words, "ab")
        self.assertItemsEqual(got, range(len(raw)))
        got = gm(words, "abb")
        self.assertItemsEqual(got, range(len(raw)-1))
        got = gm(words, "abbb")
        self.assertItemsEqual(got, range(3))

    @unittest.skip("wait")
    def test_temp(self):
        #import pdb;pdb.set_trace()
        got = self.s.wordSquares(self.s.words)
        print got

    #@unittest.skip("wait")
    def test_solution(self):
        words = self.s.words 
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
