class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        for item in tokens:
            # find an arithmetic symbol
            if item in "*-+/":
                item1 = int(stack.pop())
                item2 = int(stack.pop())

                print(item1, item2)
                result = None
                match item:
                    case "*":
                        result = item2 * item1
                    case "-":
                        result = item2 - item1
                    case "+":
                        result = item2 + item1
                    case "/":
                        result = item2 / item1
                stack.append(result)

            else:
                stack.append(item)

        return int(stack[-1])