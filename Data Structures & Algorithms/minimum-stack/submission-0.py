class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        self.min_stack = [val] + self.min_stack

        if len(self.min_stack) == 1:
            self.minimum = val
        else:
            if val < self.minimum:
                self.minimum = val

    def pop(self) -> None:
        self.min_stack.pop(0)

    def top(self) -> int:
        return self.min_stack[0]

    def getMin(self) -> int:
        return min(self.min_stack)
