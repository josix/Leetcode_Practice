class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        from sys import maxsize
        self.min = maxsize
        

    def push(self, x: int) -> None:
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
                              
    def pop(self) -> None:
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
