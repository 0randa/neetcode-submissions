class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = []

        for t in tokens:
            match t:
                case "+":
                    # pop the 2 elements and add them, and then add them to the set
                    num1, num2 = stack.pop(), stack.pop()
                    stack.append(num1 + num2)
                case "*":
                    num1, num2 = stack.pop(), stack.pop()

                    # ..., multiply, ...
                    stack.append(num1 * num2)

                case "-":
                    num1, num2 = stack.pop(), stack.pop()

                    # ..., subtract, ...
                    stack.append(num1 - num2)

                case "/":
                    num1, num2 = stack.pop(), stack.pop()
                    stack.append(num1 / num2)

                    # ..., divide, ...

                case _:
                    print("hi")
                    stack.append(int(t))
                    # add the element to the queue

        return stack[0]
                