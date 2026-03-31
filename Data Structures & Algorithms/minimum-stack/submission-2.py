class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_num_tracking_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_num_tracking_stack or val < self.min_num_tracking_stack[-1]:
            self.min_num_tracking_stack.append(val)
        else:
            self.min_num_tracking_stack.append(self.min_num_tracking_stack[-1])

    def pop(self) -> None:
        self.main_stack.pop(-1)
        self.min_num_tracking_stack.pop(-1)

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_num_tracking_stack[-1]
