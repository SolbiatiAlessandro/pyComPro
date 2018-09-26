class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in set(['(','{','[']):
                stack.append(c)
            elif c == ')':
                if len(stack)>0 and stack[-1] == '(':
                    stack.pop()
                else :
                    return False
            elif c == ']':
                if len(stack)>0 and  stack[-1] == '[':
                    stack.pop()
                else :
                    return False
            elif c == '}':
                if len(stack)>0 and  stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return not len(stack)
