class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        # add all the right brackets into the stack
        stack = []

        for brac in s:
            # push opening brackets into the stack
            if brac in mapping:
                stack.append(brac)
            # if its a closing bracket, pop the stack and compare the elements
            else:
                if not stack:
                    return False
                # pop the stack
                top = stack.pop()
                # if they're not matching brackets, return false
                if mapping[top] != brac:
                    print(brac)
                    return False



        # stack has to be empty
        print(stack, "is empty", not stack)
        return not stack
