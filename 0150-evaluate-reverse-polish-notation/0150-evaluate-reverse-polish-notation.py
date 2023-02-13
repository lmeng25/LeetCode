class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        while tokens:
            curr = tokens.pop(0)
            if curr not in operators:
                stack.append(int(curr))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if curr == "+":
                    stack.append(num1 + num2)
                elif curr == "-":
                    stack.append(num1 - num2)
                elif curr == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
        
        return stack.pop()
                    