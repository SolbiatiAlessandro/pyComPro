class Solution():
    def wildcard(self, words, board):
        def solve(y, x, word, visited):
            if not word: return True
            for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                if 0 <= y+i < len(board)      and\
                   0 <= x+j < len(board[0])   and\
                   board[y+i][x+j] == word[0] and\
                   (y+i,x+j) not in visited:
                       s = visited.copy()
                       s.add((y+i,x+j))
                       got = solve(y+i, x+j, word[1:], s)
                       if got: return True
            return False

        from collections import defaultdict
        d = defaultdict(list)
        for i, col in enumerate(board):
            for j, row in enumerate(col):
                d[row].append((i,j))
        res = [0 for _ in words]
        for i, word in enumerate(words):
            for start in d[word[0]]:
                if not res[i] and solve(start[0],start[1],word[1:],set([(start[0],start[1])])):
                    res[i] = 1
        return [word for i, word in enumerate(words) if res[i]]


if __name__ == "__main__":
    ss=Solution()
    words = ["oath","pea","eat","rain","oateo"] 
    board =[
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    assert set(ss.wildcard(words, board)) == set(["eat","oath"])
