import unittest
from robot import Robot
import l1340

class testSolution(unittest.TestCase):
    def setUp(self):
        self.s = l1340.Solution()

    #@unittest.skip("Wait")
    def test_2x2(self):
        grid = [[1, 1], [1, 1]]
        robot = Robot(1, 1, grid)
        #import pdb;pdb.set_trace()
        self.s.cleanRoom(robot)
        for i in grid:
            for j in i:
                self.assertEqual(j, 'C')
        #robot._debug()

    def test_4x2(self):
        grid = [[1, 1, 1, 1], [1, 1, 1, 1]]
        robot = Robot(1, 1, grid)
        #import pdb;pdb.set_trace()
        self.s.cleanRoom(robot)
        #robot._debug()
        for i in grid:
            for j in i:
                self.assertEqual(j, 'C')

    def test_4x5(self):
        grid = [[1, 1, 1, 1], [1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]]
        robot = Robot(1, 1, grid)
        #import pdb;pdb.set_trace()
        self.s.cleanRoom(robot)
        #robot._debug()
        for i in grid:
            for j in i:
                self.assertEqual(j, 'C')

    def test_4x5_obstacles(self):
        grid = [[1, 1, 1, 1], [1, 0, 1, 1],[1, 1, 0, 0],[1, 0, 1, 1],[1, 1, 1, 1]]
        robot = Robot(1, 1, grid)
        #import pdb;pdb.set_trace()
        self.s.cleanRoom(robot)
        #robot._debug()
        for i in grid:
            for j in i:
                if j != 0:
                    self.assertEqual(j, 'C')

    def test_custom_map(self):
        grid = [[1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0],[0, 1, 0, 1, 1, 0],[0, 1, 1, 1, 1, 0],[0, 1, 0, 1, 1, 1],[1, 1, 1, 0, 0, 0],[1, 1, 1, 0, 0, 0]]
        robot = Robot(3, 4, grid)
        #import pdb;pdb.set_trace()
        self.s.cleanRoom(robot)
        #robot._debug()
        for i in grid:
            for j in i:
                if j != 0:
                    self.assertEqual(j, 'C')

    def test_leetcode_example(self):
        room = [
          [1,1,1,1,1,0,1,1],
          [1,1,1,1,1,0,1,1],
          [1,0,1,1,1,1,1,1],
          [0,0,0,1,0,0,0,0],
          [1,1,1,1,1,1,1,1]
        ]
        row = 1
        col = 3
        robot = Robot(row, col, room)
        #import pdb;pdb.set_trace()
        self.s.cleanRoom(robot)
        #robot._debug()
        for i in room:
            for j in i:
                if j != 0:
                    self.assertEqual(j, 'C')





if __name__ == "__main__":
    unittest.main()
