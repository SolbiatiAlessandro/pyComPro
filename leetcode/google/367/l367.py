class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        answers = {}
        def solve(week, city):
            """recursive call for the DP problem, returns (int) answer"""
            if week == len(days[0]): return 0
            if answers.get((week, city)) is None: 
                answers[(week, city)] = max([solve(week + 1, j) + days[j][week] 
                        for j in xrange(len(flights)) if (flights[city][j] or j == city)])
            return answers[(week, city)]
        return solve(0, 0)
