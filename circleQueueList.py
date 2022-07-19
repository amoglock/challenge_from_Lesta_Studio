class MyCircularQueue:
    """The creation object circular queue"""

    def __init__(self, k):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.k = k
        self.q = [None] * k


    def enqueue(self, value):
        """Add new item in queue if it not full"""

        if self.is_full():
            return "{} is not was apended. Queue is full!".format(value)

        self.q[self.tail] = value
        self.size += 1
        self.tail = (self.tail + 1) % self.k
        return "{} in queue".format(value)


    def dequeue(self):
        """Remove and return item from queue if it not empty"""
        if self.is_empty():
            return "Failed to execute. The queue is empty!"
        item = self.q[self.head]
        self.q[self.head] = None
        self.size -= 1
        self.head = (self.head + 1) % self.k
        return item


    def next_item(self):
        """Return first element in queue.
        If queue is empty return -1"""

        if self.is_empty():
            return -1
        return self.q[self.head]


    def last_item(self):
        """Return last element in queue.
        If queue is empty return -1"""

        if self.is_empty():
            return -1
        return self.q[self.tail - 1]


    def is_empty(self):
        """Return True if queue is empty, else False"""

        if self.size == 0:
            return True
        return False


    def is_full(self):
        """Return True if queue is full, else False"""

        if self.size == self.k: return True
        return False


    def return_queue(self):
        """Return all elements in queue if not empty"""

        if not self.is_empty():
            return [x for x in self.q if x is not None]


a = MyCircularQueue(3)