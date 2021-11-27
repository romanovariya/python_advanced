class Queue:
    def __init__(self):
        self.pop_stack = []
        self.push_stack = []

    def push(self, x):
        self.push_stack.append(x)
        self.pop_stack = self.push_stack[::-1]

    def pop(self):
        if len(self.pop_stack) == 0:
            raise IndexError('pop from an empty queue')
        else:
            res = self.pop_stack.pop()
            self.push_stack = self.pop_stack[::-1]
            return res
