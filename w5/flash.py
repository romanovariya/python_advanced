class FlashError(Exception):
    pass


class FlashMaxFileSizeError(Exception):
    pass


class FlashMemoryLimitError(Exception):
    pass


class Flash:
    def __init__(self, capacity, max_file_size=None):
        self.capacity = capacity
        self.storage = 0
        self.max_file = max_file_size

    def write(self, file_size):
        if self.max_file is not None:
            if file_size > self.max_file:
                raise FlashMaxFileSizeError
            else:
                pass
        if file_size + self.storage > self.capacity:
            raise FlashMemoryLimitError
        else:
            self.storage += file_size
