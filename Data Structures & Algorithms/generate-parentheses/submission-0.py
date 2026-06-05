class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ret_array = []
        parenthesis = self.generate_strings(n)

        for string in parenthesis:
            if self.isValid(string):
                ret_array.append(string)

        return ret_array

    def generate_strings(self, n):
        from itertools import product

        combinations = product('()', repeat = 2*n)

        return [''.join(comb) for comb in combinations]


    def isValid(self, s: str) -> bool:
        # loop through the string and add the characters into the stack

        if len(s) % 2 != 0:
            return False

        mapping = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        stack = []

        for char in s:
            # if the char is in mapping, peek the stack
            if char in mapping:
                if not stack:
                    return False
                top = stack[-1]
                if mapping[char] != top:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        if len(stack) != 0:
            return False

        return True