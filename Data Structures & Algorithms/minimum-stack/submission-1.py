class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_val_at_each_depth_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)

        if len(self.min_stack) == 1:
            self.min_val_at_each_depth_stack.append(val)
        else:
            self.min_val_at_each_depth_stack.append(min(val, self.min_val_at_each_depth_stack[-1]))
                

    def pop(self) -> None:
        self.min_stack.pop(-1)
        self.min_val_at_each_depth_stack.pop(-1)

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_val_at_each_depth_stack[-1]
