import unittest
import word_ladder


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = word_ladder.Solution()

    def test_solution( self ):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        got = self.s.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(got, 5)

    def test_profile(self):
        import custom
        import time
        t1 = time.time()
        got = self.s.ladderLength(custom.beginWord, custom.endWord, custom.wordList)
        t2 = time.time()
        print t2 - t1

        

if __name__ == "__main__":
    unittest.main()

