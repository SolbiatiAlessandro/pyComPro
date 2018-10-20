def binary_search(sorted_words, query):
    """given a string query return the index in words where the string matches

    Args:
        words: (list[str, original_index]) sorted vector of words
        query: (str) like "ba" (from "ball")
    Returns:
        integer: index of a match of 'query' in words
        integer: index of match in sorted_words
    """
    a, b, query_len = 0, len(sorted_words)-1, len(query)
    while b >= a:
        m = (b-a)/2 + a
        comparison_string = sorted_words[m][0][:query_len]
        if comparison_string == query:
            return sorted_words[m][1], m
        elif comparison_string > query:
            b = m-1
        else:
            a = m+1
    return -1, -1


def get_matches(sorted_words, query):
    """given a list of words and a query return a list of index of all
    the matches for that query

    Args:
        sorted_words: (list[str, original_index]) sorted vector of words
        query: (str) like "ba" (from "ball")
    Returns:
        matches: list[int] of all words matching query
    """
    base_match, base_index = binary_search(sorted_words, query)
    if base_match == -1:
        return []
    res, len_query = [base_match], len(query)
    up, down = base_index + 1, base_index - 1
    while up < len(sorted_words) and sorted_words[up][0][:len_query] == query:
        res.append(sorted_words[up][1])
        up += 1
    while down >= 0 and sorted_words[down][0][:len_query] == query:
        res.append(sorted_words[down][1])
        down -= 1
    return res


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        sorted_words = sorted(zip(words, xrange(len(words))))
        WORD_LEN = len(words[0])
        res = []

        def solve(solution):
            """recursive call for the solution of the task

            Given a valid subsolution, iterate over all matches and call itself
            on other subsolution with length = len(solution) + 1,
            if is the desired length it appends the results to res

            Args:
                solution: list[int], list of indexes of words that build sub-solutions
            """
            if len(solution) == WORD_LEN:
                return res.append(solution[:])
            query, index = "", len(solution)
            for i in xrange(len(solution)):
                query += words[solution[i]][index]

            matches = get_matches(sorted_words, query)
            for match in matches:
                solve(solution + [match])

        for i in xrange(len(words)):
            solve([i])

        for solution_index, solution in enumerate(res):
            for word_index, word in enumerate(solution):
                res[solution_index][word_index] = words[word]
        return res
