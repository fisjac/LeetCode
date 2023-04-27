class MinStack:

    def __init__(self):
        self.current = None

    def push(self, val: int) -> None:
        if not self.current:
            self.current = Node(val)
        else:
            newNode = Node(val,min(val,self.current.stack_min))
            newNode.next = self.current
            self.current = newNode


    def pop(self) -> None:
        val = self.current.val
        self.current = self.current.next
        return val


    def top(self) -> int:
        return self.current.val

    def getMin(self) -> int:
        return self.current.stack_min

class Node:
    def __init__(self,val=None, stack_min=None):
        self.val = val
        self.stack_min = stack_min if stack_min != None else val
        self.next = None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
