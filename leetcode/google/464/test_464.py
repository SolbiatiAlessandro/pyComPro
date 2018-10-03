import unittest
import l464


class testSolution(unittest.TestCase):
    
    def setUp(self):
        self.s = l464.Solution()

    def test_Solution(self):

        array = [1,1,2]
        got = self.s.removeDuplicates(array)
        self.assertEqual(array[:got], [1,2])
        self.assertEqual(got, 2)

        array = [0,0,1,1,1,2,2,3,3,4]
        got = self.s.removeDuplicates(array)
        self.assertEqual(array[:got], [0,1,2,3,4])
        self.assertEqual(got, 5)

        array = []
        got = self.s.removeDuplicates(array)
        self.assertEqual(array[:got], [])
        self.assertEqual(got, 0)

        array = [5,5,5,5,5,5,5]
        got = self.s.removeDuplicates(array)
        self.assertEqual(array[:got], [5])
        self.assertEqual(got, 1)

        array = [5,5,4,1,1]
        got = self.s.removeDuplicates(array)
        self.assertEqual(array[:got], [5,4,1])
        self.assertEqual(got, 3)

        array = ['a','a',4,5,'k','k']
        got = self.s.removeDuplicates(array)
        self.assertEqual(array[:got], ['a',4,5,'k'])
        self.assertEqual(got, 4)

if __name__ == "__main__":
    unittest.main()

