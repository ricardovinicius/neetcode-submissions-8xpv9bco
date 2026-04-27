class MinStack:

    def __init__(self):
        self.val_stack = []
        self.min_val_stack = []
        

    def push(self, val: int) -> None:
        self.val_stack.append(val)
        if self.min_val_stack:
            if self.min_val_stack[-1] > val:
                self.min_val_stack.append(val)
            else:
                self.min_val_stack.append(self.min_val_stack[-1])
        else:
            self.min_val_stack.append(val)
        

    def pop(self) -> None:
        self.min_val_stack.pop()
        return self.val_stack.pop()

    def top(self) -> int:
        return self.val_stack[-1]

    def getMin(self) -> int:
        return self.min_val_stack[-1]
        
