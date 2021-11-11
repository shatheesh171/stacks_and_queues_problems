# Queue via stacks

class Stack:
    def __init__(self) -> None:
        self.list=[]

    def __len__(self):
        return len(self.list)

    def push(self,item):
        self.list.append(item)

    def pop(self):
        if len(self.list)==0:
            return None
        return self.list.pop()

class QueueviaStack:
    def __init__(self) -> None:
        #two stacks for moving items from in to out for dequeue and moving it back
        self.inStack=Stack()
        self.outStack=Stack()

    def enqueue(self,item):
        self.inStack.push(item)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result=self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result


cq=QueueviaStack()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.dequeue())
cq.enqueue(4)
print(cq.dequeue())