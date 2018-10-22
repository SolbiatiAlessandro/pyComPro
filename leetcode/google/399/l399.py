class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(n):
            if n == 0: return [""]
            if n == 1: return ["0","1", "8"]
            res = []
            sequences = generate(n-2)
            for sequence in sequences:
                for i in ["1","8","0"]:
                    res.append(i+sequence+i)
                res.append("6"+sequence+"9")
                res.append("9"+sequence+"6")
            return res
        res = generate(n)
        if n != 1:
            for index, sequence in enumerate(res):
                if sequence[0] == "0":
                    del(res[index])
        return res
        
