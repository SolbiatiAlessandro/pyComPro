class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [0]

        def call(pos, bitmask):
            """recursive call to solve the task

            Args:
                i: int, position on the table
                bitmask: int < 1024, bitmask to keep track of visited
            """
            bitmask = bitmask | (1 << pos)
            count = sum([1 for i in xrange(1,10) if bitmask & (1 << i)])
            if m <= count <= n: res[0] += 1
            else: return
            for next_pos in xrange(1,10):
                if next_pos != pos and not bitmask & (1 << next_pos):
                    if (
                       not pos % 2 and
                       not (next_pos + pos) % 2 and
                       next_pos != 5
                       ) or (
                       pos % 2 and
                       next_pos + pos == 10
                       ):
                        new_bitmask = bitmask | (1 << (pos + next_pos)/2)
                        call(next_pos, new_bitmask)
                    else:
                        call(next_pos, bitmask)

        call(1, 0)
        call(2, 0)
        res[0] *= 4
        call(5, 0)
        return res[0]
