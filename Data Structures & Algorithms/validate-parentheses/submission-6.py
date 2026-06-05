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
                # pop the stack
                top = stack[-1]
                # if they're not matching brackets, return false
                if mapping[stack[-1]] != brac:
                    print(brac)
                    return False
                else:
                    # pop the last element of the stack
                    stack.pop()



        # stack has to be empty
        print(stack, "is empty", not stack)
        return not stack
