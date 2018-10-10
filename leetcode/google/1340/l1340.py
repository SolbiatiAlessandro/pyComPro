"""leetcode.com/explore/interview/card/google/61/trees-and-graphs/1340/"""


class Tuple(tuple):
    """overload + for tuples with custom built class T"""
    def __add__(self, other):
        return Tuple(x+y for x, y in zip(self, other))

class Solution(object):
    def __init__(self):
        self.directions = [Tuple((0, 1)),
                           Tuple((1, 0)),
                           Tuple((0, -1)),
                           Tuple((-1, 0))]
        self.orientation = 0
        self.pos = Tuple((0, 0))
        self.cnt = 0

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        stack, visited = [self.pos], set()
        while stack:
            #import pdb;pdb.set_trace() 
            node = stack[-1]
            self.move_to(node)
            robot.clean()
            visited.add(self.pos)

            self.cnt, next_node = 0, None
            for _ in xrange(4):
                elem = self.pos + self.directions[self.orientation]
                if elem in visited:
                    self.rotate_robot()
                else:
                    if robot.move() == 0:
                        visited.add(elem)
                        self.rotate_robot()
                    else:
                        self.pos = elem
                        next_node = elem
                        break

            if self.cnt == 4:
                stack.pop()
            else:
                stack.append(next_node)

    def rotate_robot(self):
        """rotates robot of 90 degrees to the right"""
        self.cnt += 1
        self.orientation = (self.orientation + 1) % 4
        self.robot.turnRight()

    def move_to(self, where):
        """rotate the robot using .turnRight() and than move it with .move()"""
        rotate = 0
        if self.pos == where:
            return
        while self.pos + self.directions[self.orientation] != where:
            self.orientation = (self.orientation + 1) % 4
            rotate += 1
            if rotate > 4:
                exit("error: distance in stack > 1")

        if rotate == 1:
            self.robot.turnRight()
        elif rotate == 2:
            self.robot.turnRight()
            self.robot.turnRight()
        elif rotate == 3:
            self.robot.turnLeft()

        if self.pos + self.directions[self.orientation] == where:
            self.pos = where
            self.robot.move()
