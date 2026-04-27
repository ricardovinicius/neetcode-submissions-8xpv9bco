class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Since the reverse polish notation have 
        # they operands after the members
        # we can use a stack to store the tokens
        # and compute the operations in 
        # LIFO order 

        operands = ['-', '+', '*', '/']

        token = tokens.pop()

        if token in operands:
            right = self.evalRPN(tokens)
            left = self.evalRPN(tokens)
            
            if token == '-':
                return left - right
            elif token == '+':
                return left + right
            elif token == '*':
                return left * right
            else:
                return int(left / right)
        else:
            return int(token)

        