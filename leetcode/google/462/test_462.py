import unittest
import l462


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l462.Solution()
        self.words = ["area","lead","wall","lady","ball"]

    def test_trie(self):
        bt = l462.make_trie
        trie = bt(self.words)
        self.assertFalse(trie.children.get("d"))
        self.assertTrue(trie.children["l"])
        self.assertEqual(trie.children["a"].children["r"].children["e"]\
                .children["a"].index, 0)
        self.assertEqual(trie.children["b"].children["a"].children["l"]\
                .children["l"].index, 4)
        self.assertEqual(trie.children["l"].children["a"].children["d"]\
                .children["y"].index, 3)
        self.assertEqual(trie.children["w"].children["a"].children["l"]\
                .children["l"].index, 2)
        self.assertEqual(trie.children["l"].children["e"].children["a"]\
                .children["d"].index, 1)

        """ this test is useless since we add list(set(words)) condition
        words = ["aa", "ab", "ac", "ac"]
        trie = bt(words)
        self.assertEqual(trie.children['a'].children['c'].letter, 'c')
        self.assertEqual(trie.children['a'].children['b'].letter, 'b')
        self.assertEqual(trie.children['a'].children['b'].index, 1)
        self.assertEqual(trie.children['a'].children['c'].index, 2)
        """

        words = ["abcd", "ab"]
        trie = bt(words)
        self.assertEqual(trie.children['a'].children['b'].index, 1)
    
    #@unittest.skip("wait") 
    def test_solution(self):
        words = ["oath","pea","eat","rain"] 
        board = [
          ['o','a','a','n'],
          ['e','t','a','e'],
          ['i','h','k','r'],
          ['i','f','l','v']
        ]
        got = self.s.findWords(board, words)
        expected = ["eat","oath"]
        self.assertItemsEqual(got, expected)

        words = ["oath","pea","eat","rain","rained","raining","rainidi","rainedi"] 
        board = [
          ['o','a','a','n','n','i'],
          ['e','t','a','e','i','d'],
          ['i','h','k','r','a','e'],
          ['i','f','l','v','i','n']
        ]
        got = self.s.findWords(board, words)
        expected = ["eat","oath","rained","rain","rainedi"]
        self.assertItemsEqual(got, expected)

        words = ["oath","pea","eat","rain","rained","raining","rainidi","rainedi"] 
        board = []
        got = self.s.findWords(board, words)
        expected = []
        self.assertItemsEqual(got, expected)

        #import pdb;pdb.set_trace()
        board = [["a","a"]]
        words = ["aaa"]
        got = self.s.findWords(board, words)
        expected = []
        self.assertItemsEqual(got, expected)

        from custom_input import BOARD, WORDS, EXPECTED
        trie = l462.make_trie(WORDS)
        c_node = trie.children['a'].children['a'].children['a'].children['a'].children['a'].children['a'].children['a'].children['a'].children['a'].children['a'].children['a'].children['a'].children['a'].children['a'].children['c']
        self.assertTrue(c_node.children['g'])
        self.assertTrue(c_node.children['z'])
        got = self.s.findWords(BOARD, WORDS)
        self.assertItemsEqual(got, EXPECTED)

        board = [["a","b"],["c","d"]]
        words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
        #import pdb;pdb.set_trace()
        got = self.s.findWords(board, words)
        expected = ["ab","ac","bd","ca","db"]
        self.assertItemsEqual(got, expected)


if __name__ == "__main__":
    unittest.main()
