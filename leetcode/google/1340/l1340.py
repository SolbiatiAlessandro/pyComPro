"""leetcode.com/explore/interview/card/google/61/trees-and-graphs/1340/"""


class Tuple(tuple):
    """overload + for tuples with custom built class T"""
    def __add__(self, other):
        return Tuple(x+y for x, y in zip(self, other))


DIRECTIONS = [Tuple((0, 1)),
              Tuple((1, 0)),
              Tuple((0, -1)),
              Tuple((-1, 0))]

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        orientation = 0
        pos = Tuple((0, 0))
        cnt = 0
        stack, visited = [pos], set()
        while stack:

            node = stack[-1]

            if pos != node:
                while pos + DIRECTIONS[orientation] != node:
                    orientation = (orientation + 1) % 4
                    robot.turnRight()
                robot.move()
                pos = node

            robot.clean()
            visited.add(pos)

            cnt, next_node = 0, None
            for _ in xrange(4):
                elem = pos + DIRECTIONS[orientation]
                if elem in visited:
                    cnt += 1
                    orientation = (orientation + 1) % 4
                    robot.turnRight()
                else:
                    if robot.move() == 0:
                        visited.add(elem)
                        cnt += 1
                        orientation = (orientation + 1) % 4
                        robot.turnRight()
                    else:
                        pos = elem
                        next_node = elem
                        break

            if cnt == 4:
                stack.pop()
            else:
                stack.append(next_node)
