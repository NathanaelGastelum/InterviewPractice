class MinStack:


    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        # how to implement this so that push() is still O(1)
            # Priority queue is only O(log n) push()
            # Continually save the current min on a seperate stack
        self.min_stack[-1]

minStack = MinStack()

minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.getMin() # return 0
minStack.pop()
minStack.top()    # return 2
minStack.getMin() # return 1