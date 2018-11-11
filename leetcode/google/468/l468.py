class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack, operators = [], ['*','+','-','/']
        for token in tokens:
            if token not in operators: stack.append(token)
            else: 
                second_operand, first_operand = stack.pop(), stack.pop()
                string = "int(float("+first_operand+")"+token+"float("+second_operand+"))"
                stack.append(str(eval(string)))
        return int(stack[0])
