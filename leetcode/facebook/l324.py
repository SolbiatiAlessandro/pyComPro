class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def recursion(string, i, count):
            if i == len(string): return [string]
            if string[i] == "(": count += 1
            if string[i] == ")": count -= 1
            if count >= 0:
                return recursion(string, i+1, count)
            res = set()
            for index in xrange(i + 1):
                if string[index] == ")":
                    for s in recursion(string[:index] + string[index + 1:], i, 0) :
                        res.add(s)
            return res

        def reverse(string):
            rstring = ""
            for i in reversed(xrange(len(string))):
                if string[i] == "(": rstring += ")"
                elif string[i] == ")": rstring += "("
                else: rstring += string[i]
            return rstring

        res = recursion(s, 0, 0)

        res_inverted = set()
        for string in res:
            for s in recursion(reverse(string), 0, 0):
                res_inverted.add(s)

        res = [reverse(string) for string in res_inverted]
        return res

        
if __name__ == "__main__":
    s = Solution()
    string =  "()())()"
    assert sorted(s.removeInvalidParentheses(string)) == sorted(["()()()", "(())()"])
    string =  "(a)())()"
    assert sorted(s.removeInvalidParentheses(string)) == sorted(["(a)()()", "(a())()"])
    string =  ")("
    assert sorted(s.removeInvalidParentheses(string)) == sorted([""])
    print s.removeInvalidParentheses("(()))((()")
