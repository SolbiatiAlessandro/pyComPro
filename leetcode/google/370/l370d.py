from collections import defaultdict


class Node(object):
    def __init__(self, letter):
        self.char = letter
        self.children = defaultdict(list)
        self.indexes = []


def build_prefix_trie(words):
    """given a list of words build a prefix tree

    Args:
        words: list[str]

    Return:
        tree: instance of Node(), root of the (trie) tree
    """
    LEN_WORD = len(words[0])
    tree = Node('*')
    for word_index, word in enumerate(words):
        letter_index, curr = 0, tree

        while curr.children[word[letter_index]]:  # already existing
            curr = curr.children[word[letter_index]]
            curr.indexes.append(word_index)
            letter_index += 1

        while letter_index < LEN_WORD:  # create new nodes
            new_node = Node(word[letter_index])
            curr.children[word[letter_index]] = new_node
            curr = new_node
            curr.indexes.append(word_index)
            letter_index += 1
    return tree


def get_matches(trie, query):
    """
    get children from a query on the trie

    Traverse the prefix trie following the letters on query,
    once query is finished it runs a dfs to traverse all paths
    and get all children from there.

    Args:
        trie: instance of node
        query: string "ba" (from "ball")

    Returns:
        list[int] : index of matches
    """
    for letter in query:
        if trie:
            trie = trie.children[letter]
        if not trie:
            return []
    return trie.indexes


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        WORD_LEN = len(words[0])
        res = []
        trie = build_prefix_trie(words)

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
