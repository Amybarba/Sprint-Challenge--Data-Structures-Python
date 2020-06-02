class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity
        # pre_allocated_list = [None] * size
        # to pre-allocate a list (that is, to be able to address
        # 'size' elements of the list instead of gradually forming
        # the list by appending). This operation is VERY fast, even on big lists.

    def append(self, item):  # When the ring buffer is full and a new element is inserted
        self.storage[self.current] = item # self.storage will create the new list self.current
        self.current += 1
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        if self.storage[-1] is None:
            return self.storage[:self.current]  # use a slice, With slices, we can call multiple character values
        return self.storage
