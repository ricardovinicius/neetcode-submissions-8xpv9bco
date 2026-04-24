class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(':
                stack.append('(')
            if char == ')':
                last_char = stack.pop() if len(stack) else None
                if last_char != '(':
                    return False

            if char == '{':
                stack.append('{')
            if char == '}':
                last_char = stack.pop() if len(stack) else None
                if last_char != '{':
                    return False
            
            if char == '[':
                stack.append('[')
            if char == ']':
                last_char = stack.pop() if len(stack) else None
                if last_char != '[':
                    return False

        return False if len(stack) else True
            

