class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None for _ in range(k + 1)]
        self.head = 0
        self.tail = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % len(self.queue)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.head] = None
        self.head = (self.head + 1) % len(self.queue)
        return True
            

    def Front(self) -> int:
        if self.isEmpty(): 
            return -1
        return self.queue[self.head]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail - 1]
        

    def isEmpty(self) -> bool:
        return self.head == self.tail
        

    def isFull(self) -> bool:
        if self.tail < self.head:
            return self.tail + len(self.queue) - self.head == len(self.queue) - 1
        else:
            return self.tail - self.head == len(self.queue) - 1
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()