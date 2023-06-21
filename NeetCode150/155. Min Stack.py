class MinStack(object):

    def __init__(self):
        self.arr = []
        self.min_stack = []

    def __set_min_val(self, val):
        if self.min_stack:
            if self.min_stack[-1] < val:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)
        print(self.min_stack)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        self.__set_min_val(val)

        

    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()
        self.min_stack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    s.push(1)