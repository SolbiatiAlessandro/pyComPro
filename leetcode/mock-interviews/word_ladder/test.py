import unittest
import word_ladderB


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = word_ladderB.Solution()

    def test_solution( self ):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        got = self.s.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(got, 5)

        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        got = self.s.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(got, 0)

    def test_profile(self):
        import custom
        import time
        t1 = time.time()
        got = self.s.ladderLength(custom.beginWord, custom.endWord, custom.wordList)
        t2 = time.time()
        print t2 - t1

        

if __name__ == "__main__":
    unittest.main()

