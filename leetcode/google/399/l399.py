class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(n, elems):
            if n == 0: return [""]
            if n == 1: return ["0","1", "8"]
            res = []
            sequences = generate(n-2, ["0","1","8"])
            for sequence in sequences:
                for i in elems:
                    res.append(i+sequence+i)
                res.append("6"+sequence+"9")
                res.append("9"+sequence+"6")
            return res
        return generate(n, ["1","8"])
