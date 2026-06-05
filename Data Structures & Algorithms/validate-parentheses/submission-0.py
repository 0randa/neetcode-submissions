class Solution:
    def isValid(self, s: str) -> bool:
        # loop through the string and add the characters into the stack
        mapping = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        stack = []

        for char in s:
            # if the char is in mapping, peek the stack
            if char in mapping:
                
                top = stack[-1]

                if mapping[char] != top:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(char)

        return True