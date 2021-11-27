class Buffer:
    def __init__(self, maxsize):
        self.size = maxsize
        self.buffer = []

    def add(self, *a):
        for i in a:
            if len(self.buffer) < self.size:
                self.buffer.append(i)
            if len(self.buffer) >= self.size:
                res = 0
                for num in self.buffer:
                    res += num
                print(res)
                self.buffer.clear()

    def get_current_part(self):
        return self.buffer
