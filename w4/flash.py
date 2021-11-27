class Flash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = 0

    def write(self, file_size):
        if file_size + self.storage > self.capacity:
            raise ValueError
        else:
            self.storage += file_size
