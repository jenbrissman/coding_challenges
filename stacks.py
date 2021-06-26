# Implement the MaxStack class:

# MaxStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMax() retrieves the maximum element in the stack.


class Maxstack:
    def __init__(self):
        self.og_stack = []
        self.max_stack = []
    
    def push(self, x):
        self.og_stack.append(x)
        if len(self.max_stack)==0:
            self.max_stack.append(x)
        else:
            if self.max_stack[-1]<x:
                self.max_stack.append(x)
            else:
                self.max_stack.append(self.max_stack[-1])
                    
    def pop(self):
        if len(self.og_stack):
            self.og_stack.pop()
            self.max_stack.pop()
        return None

    def top(self):
        return self.og_stack[-1]

    def getMax(self):
        return self.max_stack[-1]

test = Maxstack()
test.push(2)
test.push(5)
test.push(3)
test.push(10)
test.push(12)
test.pop()
test.pop()
test.push(1000)
test.push(3)
test.push(-1)
test.push(8)
print(test.getMax())

print(test.og_stack)
print(test.max_stack)






# class Stack():

#     def __init__(self, list=[]):
#         print('init')
#         self._items = list

#     def isEmpty(self):
#         print('isEmpty')
#         return not self._items
      
#     def push(self, item):
#         print('push')
#         self._items.append(item)

#     def pop(self):
#         print('pop')
#         return self._items.pop()

#     def size(self):
#         print('size')
#         return len(self._items)
      

#     def peek(self):
#         print('peek')
#         return self._items[-1]
      
#       #testing
# stack = Stack([1, 2, 3, 4, 5])
# print(stack.pop())
# print(stack.pop())
# print(stack.peek())
# print(stack.peek())


