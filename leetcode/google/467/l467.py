class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in set(['(','{','[']):
                stack = stack + [c]
            elif c == ')':
                if len(stack)>0 and stack[-1] == '(':
                    stack = stack[:-1]
                else :
                    return False
            elif c == ']':
                if len(stack)>0 and  stack[-1] == '[':
                    stack = stack[:-1]
                else :
                    return False
            elif c == '}':
                if len(stack)>0 and  stack[-1] == '{':
                    stack = stack[:-1]
                else:
                    return False
        return not len(stack)
