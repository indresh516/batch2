class Stack:
    def __init__(self):
     self.stack = []
    def add(self, dataval):
        if dataval not in self.stack: # Use list append method to add element
            self.stack.append(dataval)
            return True
        else:
            return False
    def peek(self):# Use peek to look at the top of the stack
        return self.stack[-1]
        
AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
#print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")

print(AStack.peek())
AStack.add("Fri")
print(AStack.stack)
print(AStack.peek())