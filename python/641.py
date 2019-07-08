class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.q = [None for _ in range(k)]
        self.head = 0 # next head to insert
        self.tail = 0 # next end to insert
        self.size = 0
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size == self.k:
            return False
        else:
            self.q[self.head % self.k] = value
            self.size += 1
            self.head -= 1
            if self.head < 0:
                self.head += self.k
            if self.size == 1:
                self.tail += 1
            # print(f'insertFront {value} {self.q}')
            # print(self.head, self.tail)
            return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size == self.k:
            return False
        else:
            self.q[self.tail % self.k] = value
            self.size += 1
            self.tail += 1
            if self.size == 1:
                self.head -= 1
            if self.head < 0:
                self.head += self.k
            # print(f'insertLast {value} {self.q}')
            # print(self.head, self.tail)
            return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        else:
            self.q[(self.head + 1 ) % self.k] = None
            self.size -= 1
            self.head += 1
            if self.size == 0:
                self.head = self.tail
            # print(f'deleteFront {self.q}')
            # print(self.head, self.tail)
            return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        else:
            self.q[self.tail % self.k - 1] = None
            self.size -= 1
            self.tail -= 1
            if self.tail < 0:
                self.tail += self.k
            if self.size == 0:
                self.head = self.tail
            # print(f'deleteLast {self.q}')
            # print(self.head, self.tail)
            return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.q[(self.head + 1)  % self.k] if not self.isEmpty() else -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        index = self.tail % self.k - 1
        if index < 0:
            index += self.k
        return self.q[index]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
