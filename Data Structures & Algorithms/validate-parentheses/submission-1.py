class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "}": "{",
            "]": "[",
            ")":  "("
        }
        stack = []
        if len(s) <= 1:
            return False
        for ch in s:
            closeCh = map.get(ch, None)
            if closeCh is None:
                stack.append(ch)
            else:
                if len(stack) > 0:
                    top = stack[len(stack) - 1]
                    if closeCh == top:
                        stack.pop()
                    else:
                        stack.append(ch)
                else:
                    stack.append(ch)
        return len(stack) == 0
        