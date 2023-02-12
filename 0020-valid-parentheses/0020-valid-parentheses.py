class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []
        
        for i in range(len(s)):
            curr = s[i]
            if curr == '(' or curr == '[' or curr == '{':
                stack.append(curr)
            else:
                if len(stack) == 0:
                    return False

                top = stack[-1]
                if curr == ')':
                    if top == '(':
                        stack.pop(-1)
                    else:
                        return False
                elif curr == ']':
                    if top == '[':
                        stack.pop(-1)
                    else:
                        return False
                else:
                    if top == '{':
                        stack.pop(-1)
                    else:
                        return False         
        
        if len(stack) != 0:
            return False        
        return True