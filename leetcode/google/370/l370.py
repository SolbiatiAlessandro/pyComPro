"""interview/card/google/62/recursion-4/370/"""


def is_valid(solution):
    """
    compute if the solution (or partial solution) is valid
    Args:
        solution: list[int], of index of words

    Return:
        bool: True, False
    """
    len_solution = len(solution)
    if len_solution < 2:
        return True
    index, string = LEN - len_solution, WORDS[solution[-1]]
    for i in xrange(1, len_solution):
        if string[index + i] != WORDS[solution[len_solution-1-i]][index]:
            return False
    return True


def solve(solution):
    """
    recrusive call to compute solution
    Args:
        solution: list[int], of index of words

    Return:
        res: list[list[int]] list of solutions
    """
    if not is_valid(solution):
        return
    if len(solution) == LEN:
        return RES.append(solution[:])
    for i in xrange(0, N):
        solution.append(i)
        solve(solution)
        solution.pop()


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        global LEN
        global WORDS
        global N
        global RES
        N, LEN, WORDS, RES = len(words), len(words[0]), words, []
        solve([])

        for solution_index, solution in enumerate(RES):
            for word_index, word in enumerate(solution):
                RES[solution_index][word_index] = WORDS[word]
            RES[solution_index].reverse()
        return RES
