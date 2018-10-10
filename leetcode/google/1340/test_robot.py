import unittest
from robot import Robot

class testRobot(unittest.TestCase):
    def test_robot(self):
        room = [
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        row = 1
        col = 3
        robot = Robot(row, col, room)
        self.assertEqual(robot.orientation, 0)
        robot.clean()
        self.assertEqual(robot.cleaned[row][col], 'C')
        robot.move()
        # robot._debug()
        robot.clean()
        self.assertEqual(robot.cleaned[row-1][col], 'C')
        robot.turnRight()
        robot.move()
        robot.clean()
        # robot._debug()
        self.assertEqual(robot.cleaned[row-1][col+1], 'C')
        robot.turnRight()
        robot.move()
        robot.clean()
        # robot._debug()
        self.assertEqual(robot.cleaned[row][col+1], 'C')
        robot.turnRight()
        robot.move()
        robot.clean()
        # robot._debug()
        self.assertEqual(robot.cleaned[row][col], 'C')
        robot.turnRight()
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.clean()
        self.assertEqual(robot.cleaned[0][col], 'C')
        self.assertEqual(robot.x, 0)
        robot.turnLeft()
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.clean()
        self.assertEqual(robot.cleaned[0][0], 'C')
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 0)


if __name__ == "__main__":
    unittest.main()
