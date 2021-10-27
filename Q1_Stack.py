#Use a single list to implement 3 stacks
#Solving it with a fixed division approach

class MultiStack:
    def __init__(self,stacksize) -> None:
        self.numberstacks=3
        #A custom list, encompassing the size of 3 stacks
        self.custList=[0]*(stacksize*self.numberstacks)
        # A list of size for each number of stack, mostly to check if its empty or not
        self.sizes=[0]*self.numberstacks
        #Stacksize can be used in other functions
        self.stacksize=stacksize

    def isFull(self,stacknum):
        if self.sizes[stacknum]==self.stacksize:
            return True
        return False

    def isEmpty(self,stacknum):
        if self.sizes[stacknum]==0:
            return True
        return False

    # A helper method
    def indexOfTop(self,stacknum):
        offset=stacknum*self.stacksize
        # offset gets the first element of stack, in this case 0,3,6 which in list correspond to first element
        # of each stack. But we need the top element so we have to add the number of non-empty
        # elements to the offset to return index of top as stack follows LIFO
        return offset+self.sizes[stacknum]

    def push(self,stacknum,value):
        #Check if stack is full
        if self.isFull(stacknum):
            return "Stack is already full"
        self.custList[self.indexOfTop(stacknum)]=value
        self.sizes[stacknum]+=1

    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            return "No elements in stack"
        value=self.custList[self.indexOfTop(stacknum)-1]
        self.custList[self.indexOfTop(stacknum)-1]=0
        self.sizes[stacknum]-=1
        return value

    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            return "No elements in stack"
        return self.custList[self.indexOfTop(stacknum)-1]
        

cs=MultiStack(3)
cs.push(0,1)
cs.push(0,2)
cs.push(0,3)
cs.push(2,5)
print(cs.pop(0))
print(cs.peek(0))
print(cs.custList)
