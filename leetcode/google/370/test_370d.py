
import unittest
import l370d


class testSolution(unittest.TestCase):

    def setUp(self):
        self.s = l370d.Solution()
        self.words = ["area","lead","wall","lady","ball"]
        self.s.words = ["area","lead","wall","lady","ball"]

    def test_trie(self):
        bt = l370d.build_prefix_trie
        trie = bt(self.words)
        self.assertEqual(trie.char, '*')
        self.assertFalse(trie.children["d"])
        self.assertTrue(trie.children["l"])
        self.assertEqual(trie.children["a"].children["r"].children["e"]\
                .children["a"].indexes, [0])
        self.assertEqual(trie.children["b"].children["a"].children["l"]\
                .children["l"].indexes, [4])
        self.assertEqual(trie.children["l"].children["a"].children["d"]\
                .children["y"].indexes, [3])
        self.assertEqual(trie.children["w"].children["a"].children["l"]\
                .children["l"].indexes, [2])
        self.assertEqual(trie.children["l"].children["e"].children["a"]\
                .children["d"].indexes, [1])
        self.assertItemsEqual(trie.children["l"].indexes, [1,3])


    #@unittest.skip("wait")
    def test_get_matches(self):
        gm = l370d.get_matches
        words = l370d.build_prefix_trie(self.s.words)
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
        words = l370d.build_prefix_trie(raw)
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
