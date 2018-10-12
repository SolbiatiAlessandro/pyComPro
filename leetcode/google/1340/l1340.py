"""leetcode.com/explore/interview/card/google/61/trees-and-graphs/1340/"""


class Tuple(tuple):
    """overload + for tuples with custom built class T"""
    def __add__(self, other):
        return Tuple(x+y for x, y in zip(self, other))

    def __sub__(self, other):
        return Tuple(x-y for x, y in zip(self, other))

    def distance(self):
        """compute metric distance for tuple representing
        (x, y) on a cartesian grid"""
        return abs(self[0])+abs(self[1])


SEQ = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def move_to(robot, direction, start, end):
    """move_to procedure to make the robot move
    Args:
        robot: Robot instance
        direction: (0, 1) ..
        start: (x,y)
        end: (x,y), important |end - start| == 1
    Returns:
        new_directions, end
    """
    first, new_direction = SEQ.index(direction), end - start
    second = SEQ.index(new_direction)
    rotations = second - first if second > first else second + 4 - first
    if rotations == 1:
        robot.turnRight()
    elif rotations == 2:
        robot.turnRight(); robot.turnRight()
    elif rotations == 3:
        robot.turnLeft()
    moved = robot.move()
    return new_direction, end if moved else start


class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        pos, direction = Tuple((0, 0)), Tuple((0, 1))
        stack, visited, prev = [pos], set(), {}
        while stack:
            node = stack.pop()

            # moves robot to node
            while (pos - node).distance() > 1:
                direction, pos = move_to(robot, direction, pos, prev[pos])
            if (pos - node).distance() == 1:
                direction, pos = move_to(robot, direction, pos, node)

            # clean and get adj
            robot.clean()
            visited.add(node)
            for adj in [Tuple((pos[0], pos[1]+1)), Tuple((pos[0], pos[1]-1)),
                        Tuple((pos[0]+1, pos[1])), Tuple((pos[0]-1, pos[1]))]:
                if adj not in visited:
                    stack.append(adj)
                    prev[adj] = pos
