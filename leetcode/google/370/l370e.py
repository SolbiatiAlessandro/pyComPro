from collections import defaultdict

def build_table(words):
    """create hashtable of substring = list[index], from words"""
    table = defaultdict(list)
    for index, word in enumerate(words):
        subword = ""
        for char in word:
            subword+=char
            table[subword].append(index)
    return table


def get_matches(table, query):
    """get children from a query on hash-table"""
    return table[query]


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        WORD_LEN = len(words[0])
        res = []
        trie = build_table(words)

        def solve(solution):
            """recursive call for the solution of the task

            Given a valid subsolution, iterate over all matches and call itself
            on other subsolution with length = len(solution) + 1,
            if is the desired length it appends the results to res

            Args:
                solution: list[int], list of indexes of words of sub-solutions
            """
            if len(solution) == WORD_LEN:
                return res.append(solution[:])
            query, index = "", len(solution)
            for i in xrange(len(solution)):
                query += words[solution[i]][index]

            matches = get_matches(trie, query)
            for match in matches:
                solve(solution + [match])

        for i in xrange(len(words)):
            solve([i])

        for solution_index, solution in enumerate(res):
            for word_index, word in enumerate(solution):
                res[solution_index][word_index] = words[word]
        return res
