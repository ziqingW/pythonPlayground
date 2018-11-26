# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0
        self.mini = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.size == 0:
            self.mini = x
            self.stack.append(x)
        else:
            if x < self.mini:
                new_x = 2*x - self.mini
                self.mini = x
                self.stack.append(new_x)
            else:
                self.stack.append(x)
        self.size += 1
        
    def pop(self):
        """
        :rtype: void
        """
        if self.size > 0:
            topNum = self.stack.pop()
            if topNum < self.mini:
                self.mini = 2*self.mini - topNum
            self.size -= 1
        
    def top(self):
        """
        :rtype: int
        """
        if self.size > 0:
            topNum = self.stack[-1]
            if topNum < self.mini:
                return self.mini
            return topNum
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.size > 0:
            return self.mini
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#  another simpler method, 
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.ministack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.ministack) > 0:
            self.ministack.append(min(self.ministack[-1], x))
        else:
            self.ministack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.ministack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.ministack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()