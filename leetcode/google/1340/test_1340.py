import unittest
from robot import Robot
import l1340
from l1340 import Tuple

class testSolution(unittest.TestCase):
    def setUp(self):
        self.s = l1340.Solution()

    def test_move_to(self):
        # testing up
        grid = [[1, 1, 1, 1], [1, 1, 1, 1]]
        robot = Robot(1, 1, grid)
        got_direction, got_pos = l1340.move_to(robot, Tuple((0,1)), Tuple((0,0)), Tuple((0,1)))
        self.assertEqual(got_direction, Tuple((0,1)))  
        self.assertEqual(got_pos, Tuple((0,1)))  
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 1)
        
        # testing left
        grid = [[1, 1, 1, 1], [1, 1, 1, 1]]
        robot = Robot(1, 1, grid)
        got_direction, got_pos = l1340.move_to(robot, Tuple((0,1)), Tuple((0,0)), Tuple((-1,0)))
        self.assertEqual(got_direction, Tuple((-1,0)))  
        self.assertEqual(got_pos, Tuple((-1,0)))  
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 0)
        
        # testing right
        grid = [[1, 1, 1, 1], [1, 1, 1, 1]]
        robot = Robot(1, 1, grid)
        got_direction, got_pos = l1340.move_to(robot, Tuple((0,1)), Tuple((0,0)), Tuple((1,0)))
        self.assertEqual(got_direction, Tuple((1,0)))  
        self.assertEqual(got_pos, Tuple((1,0)))  
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)

        # testing down
        grid = [[1, 1, 1, 1], [1, 1, 1, 1]]
        robot = Robot(1, 1, grid)
        got_direction, got_pos = l1340.move_to(robot, Tuple((0,1)), Tuple((0,0)), Tuple((0,-1)))
        self.assertEqual(got_direction, Tuple((0,-1)))  
        self.assertEqual(got_pos, Tuple((0, 0)))
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)
        
        # testing down -> right
        grid = [[1, 1, 1, 1], [1, 1, 1, 1]]
        robot = Robot(1, 1, grid)
        robot.turnRight()
        robot.turnRight()
        got_direction, got_pos = l1340.move_to(robot, Tuple((0,-1)), Tuple((0,0)), Tuple((1,0)))
        self.assertEqual(got_direction, Tuple((1,0)))  
        self.assertEqual(got_pos, Tuple((1,0)))  
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)

        print ("okk")
        
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

    #@unittest.skip("Wait")
    def test_4x2(self):
        grid = [[1, 1, 1, 1], [1, 1, 1, 1]]
        robot = Robot(1, 1, grid)
        #import pdb;pdb.set_trace()
        self.s.cleanRoom(robot)
        #robot._debug()
        for i in grid:
            for j in i:
                self.assertEqual(j, 'C')

    #@unittest.skip("Wait")
    def test_4x5(self):
        grid = [[1, 1, 1, 1], [1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]]
        robot = Robot(1, 1, grid)
        #import pdb;pdb.set_trace()
        self.s.cleanRoom(robot)
        #robot._debug()
        for i in grid:
            for j in i:
                self.assertEqual(j, 'C')

    #@unittest.skip("Wait")
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

    #@unittest.skip("Wait")
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

    #@unittest.skip("Wait")
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
