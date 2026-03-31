class MinStack:

    def __init__(self):
        self.min_stack = []
        self.minimum_val_tracker = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if not self.minimum_val_tracker:
            self.minimum_val_tracker.append(val)
        elif self.minimum_val_tracker[-1] > val:
            self.minimum_val_tracker.append(val)
        else:
            self.minimum_val_tracker.append(self.minimum_val_tracker[-1])
    
    def pop(self) -> None:
        self.min_stack.pop(-1)
        self.minimum_val_tracker.pop(-1)

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.minimum_val_tracker[-1]
