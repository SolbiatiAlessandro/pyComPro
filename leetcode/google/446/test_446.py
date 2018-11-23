import unittest
import l446


class testSolution(unittest.TestCase):
    
    def test_solution(self):
        toe = l446.TicTacToe(3)

        got = toe.move(0, 0, 1)
        self.assertEqual(got, 0)

        got = toe.move(0, 2, 2)
        self.assertEqual(got, 0)

        got = toe.move(2, 2, 1)
        self.assertEqual(got, 0)

        got = toe.move(1, 1, 2)
        self.assertEqual(got, 0)

        got = toe.move(2, 0, 1)
        self.assertEqual(got, 0)

        got = toe.move(1, 0, 2)
        self.assertEqual(got, 0)

        got = toe.move(2, 1, 1)
        self.assertEqual(got, 1)


if __name__ == "__main__":
    unittest.main()
