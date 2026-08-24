class MinStack:

    def __init__(self):
        # min = float('inf') - nothing > inf, just to help address 1st appended value as 1st min
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        # stack stores how far current min is from appended value (- or +)
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        # pop < 0 means we removed current min, so 'self.min - pop' brings back old min
        # min = 2, pop = -2 - '2 - - 2 = 4'. Old min = 4 because removed min, 2, was -2 below old min
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        # if top > 0, 'top + self.min' gets original decoded value, otherwise return min since we're
        # already tracking it
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
        
