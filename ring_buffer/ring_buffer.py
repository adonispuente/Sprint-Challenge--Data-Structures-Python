class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.count = 0

    def append(self, item):
        if self.count == self.capacity:
            self.count = 0

        if len(self.data) == self.capacity:
            self.data.pop(self.count)
            self.data.insert(self.count, item)
            self.count += 1
        if len(self.data) < self.capacity:
            self.count += 1
            self.data.append(item)

    def get(self):
        return self.data
