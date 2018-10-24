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
            
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        words = list(set(words))
        res, trie, positions = set(), make_trie(words), defaultdict(list)

        for y in xrange(len(board)):
            for x in xrange(len(board[y])):
                positions[board[y][x]].append((x, y))

        def call(x, y, node, visited):
            """recursive call the run over thourgh the trie
            and the board at the same time
            Args:
                x, y : (int, int) position on the board
                node: instance of trie Node
            """
            if x == 1 and y == 4 and len(words) == 1000 and node.children: 
                #import pdb;pdb.set_trace() 
                pass
            visited[(x, y)] = True
            if hasattr(node, 'index'):
                res.add(words[node.index])
            for letter, child in node.children.items():
                for X, Y in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                    if not visited[(X, Y)] and\
                       0 <= Y < len(board) and\
                       0 <= X < len(board[0]) and\
                       board[Y][X] == letter:
                        call(X, Y, child, visited.copy())

        for letter, branch in trie.children.items():
            for x, y in positions[letter]:
                call(x, y, branch, defaultdict(bool))
        return list(res)
