class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.queue2 == []:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.pop(0))
        res = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res
        
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
