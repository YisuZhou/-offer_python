'''
用两个栈实现队列
'''

class stack:
    def __init__(self):
        self.stack = []
    def append(self,x):
        self.stack.append(x)
    def pop(self):
        self.stack.pop()

class Solution:
    def __init__(self):
        self.stack1 = stack().stack#本体
        self.stack2 = stack().stack

    def in_queue(self,input_node):
        self.stack1.append(input_node)

    def del_queue(self):
        while(self.stack1):#全部倒在2
            self.stack2.append(self.stack1.pop())

        self.del_node = self.stack2.pop()
        while(self.stack2):
            self.stack1.append(self.stack2.pop())
        return self.del_node


if __name__ == '__main__':
    x = Solution()
    x.in_queue(1)
    x.in_queue(2)
    x.in_queue(3)
    print(x.del_queue())
    print(x.stack1)
    
    
