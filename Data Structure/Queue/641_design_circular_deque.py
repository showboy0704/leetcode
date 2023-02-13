class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [None for _ in range(k)]
        self.head = self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = 0
        else:
            self.head = (self.head-1) % len(self.queue)
        self.queue[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = 0
        else:
            self.tail = (self.tail+1) % len(self.queue)
        self.queue[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.queue[self.head] = None
            self.head = (self.head+1) % len(self.queue)

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.queue[self.tail] = None
            self.tail = (self.tail-1) % len(self.queue)

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.isEmpty():
            return False
        if (self.tail+1) % len(self.queue) == self.head:
            return True
        else:
            return False
