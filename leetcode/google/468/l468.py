class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack, operators = [], ['*','+','-','/']
        for token in tokens:
            if token == "/":
                second_operand, first_operand = stack.pop(), stack.pop()
                res = int(float(first_operand)/float(second_operand))
            elif token == "+":
                second_operand, first_operand = stack.pop(), stack.pop()
                res = int(first_operand)+int(second_operand)
            elif token == "-":
                second_operand, first_operand = stack.pop(), stack.pop()
                res = int(first_operand)-int(second_operand)
            elif token == "*":
                second_operand, first_operand = stack.pop(), stack.pop()
                res = int(first_operand)*int(second_operand)
            else:
                res = token
            stack.append(res)
        return int(stack[0])
