from collections import defaultdict


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        word_len = len(words[0])
        res, ending_letter = [], defaultdict(list)

        for index, word in enumerate(words):
            ending_letter[word[-1]].append((index, word))

        def solve(solution):
            len_solution = len(solution)
            if len_solution == word_len:
                return res.append(solution[:])

            base = words[solution[0]]
            candidates = ending_letter[base[-(len_solution + 1)]]
            for index, candidate in candidates:
                valid = True
                for j in xrange(1, len_solution):
                    if valid and words[solution[j]][-(len_solution+1)] !=\
                            candidate[-(j+1)]:
                        valid = False
                if valid:
                    solution.append(index)
                    solve(solution)
                    solution.pop()

        # here could use bitmask optimization
        for index, _ in enumerate(words):
            solve([index])

        for solution_index, solution in enumerate(res):
            for word_index, word in enumerate(solution):
                res[solution_index][word_index] = words[word]
            res[solution_index].reverse()
        return res
