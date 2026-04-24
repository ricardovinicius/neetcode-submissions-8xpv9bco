class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in close_to_open_map:
                if not stack or stack.pop() != close_to_open_map[char]:
                    return False
            else:
                stack.append(char)


        return False if stack else True
            

