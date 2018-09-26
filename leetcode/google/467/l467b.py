class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, oset = [], set(['(','{','['])
        if len(s)%2 != 0:
            return False
        for c in s:
            if c in oset:
                stack.append(c)
            elif c == ')':
                try:
                    if stack.pop() != '(':
                        return False
                except:
                    return False
            elif c == ']':
                try:
                    if stack.pop() != '[':
                        return False
                except:
                    return False
            elif c == '}':
                try:
                    if stack.pop() != '{':
                        return False
                except:
                    return False
        return not len(stack)
