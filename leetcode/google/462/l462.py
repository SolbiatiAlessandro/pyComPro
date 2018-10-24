from collections import defaultdict

class Node(object):
    def __init__(self, letter):
        self.letter = letter
        self.children = {}


def make_trie(words):
    """build trie from list of words

    Args:
        words: list(str)
    Returns:
        trie: Node, root of the trie
    """
    trie = Node('')
    for word_index, word in enumerate(words):
        prev, curr = None, trie
        index = 0
        while curr and index < len(word):
            prev = curr
            curr = curr.children.get(word[index])
            if curr:
                if index == len(word) - 1:
                    curr.index = word_index
                    continue
                index += 1
        curr = prev
        if not curr:
            exit('curr is None')
        while index < len(word):
            new_node = Node(word[index])
            curr.children[word[index]] = new_node
            curr = new_node
            index += 1
        curr.index = word_index
    return trie


def clean_words(words, cardinality):
    """clean words to avoid un-necessary recursions
    - removes duplicate using set
    - count if letter frequency is higher than the one in the board

    Args:
        words: list[str]
        cardinality: defaultdict(int) for letter fre

    Returns:
        res: list[str]
    """
    res = set()
    for word in words:
        word_cardinality, clean = defaultdict(int), True
        for letter in word:
            word_cardinality[letter] += 1
        for letter, frequency in word_cardinality.items():
            if clean and cardinality[letter] < frequency:
                clean = False
        if clean:
            res.add(word)
    return list(res)

            
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        cardinality = defaultdict(int)
        visited, positions = defaultdict(int), defaultdict(list)

        for y in xrange(len(board)):
            for x in xrange(len(board[y])):
                positions[board[y][x]].append((x, y))
                cardinality[board[y][x]] += 1

        words = clean_words(words, cardinality)
        res, trie = set(), make_trie(words)

        def call(x, y, node):
            """recursive call the run over thourgh the trie
            and the board at the same time
            Args:
                x, y : (int, int) position on the board
                node: instance of trie Node
            """
            visited[(x, y)] = 1
            if hasattr(node, 'index'):
                res.add(words[node.index])
            for letter, child in node.children.items():
                for X, Y in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                    if visited[(X, Y)] != 1   and\
                       0 <= Y < len(board)    and\
                       0 <= X < len(board[0]) and\
                       board[Y][X] == letter:
                        call(X, Y, child)
            visited[(x, y)] = 2

        for letter, branch in trie.children.items():
            for x, y in positions[letter]:
                visited.clear()
                call(x, y, branch)
        return list(res)
