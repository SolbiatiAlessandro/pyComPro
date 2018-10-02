import unittest
import l459


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l459.Solution()

    def test_solution(self):
        ss = "leetcode"
        self.assertEqual(self.s.firstUniqChar(ss), 0)

        ss = "loveleetcode"
        self.assertEqual(self.s.firstUniqChar(ss), 2)

        ss = ""
        self.assertEqual(self.s.firstUniqChar(ss), -1)

        ss = "aaaa"
        self.assertEqual(self.s.firstUniqChar(ss), -1)
        ss = "ajaaa"
        self.assertEqual(self.s.firstUniqChar(ss), 1)


if __name__ == "__main__":
    unittest.main()

