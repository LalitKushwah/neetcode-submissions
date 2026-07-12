import math

class MinStack:

    def __init__(self):
        self.stack = []    

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        return None
        
    def getMin(self) -> int:
        min_num = math.inf
        for num in self.stack:
            min_num = min(min_num, num)
        return min_num
        
