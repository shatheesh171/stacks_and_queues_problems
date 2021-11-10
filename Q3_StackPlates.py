# Stack of Plates
class PlateStack:
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.stacks=[]

    def __str__(self) -> str:
        return str(self.stacks)

    def push(self,item):
        if len(self.stacks)>0 and len(self.stacks[-1])<self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        # this is to remove empty list at the end of stacks (nested list)
        while len(self.stacks) and len(self.stacks[-1])==0:
            self.stacks.pop()
        if len(self.stacks)==0:
            return None
        return self.stacks[-1].pop()

    def pop_at(self,stackNum):
        if len(self.stacks[stackNum])>0:
            return self.stacks[stackNum].pop()
        return None


cs=PlateStack(2)
cs.push(1)
cs.push(2)
cs.push(3)
cs.push(4)
print(cs)
print(cs.pop())
print(cs.pop_at(0))
print(cs.pop_at(1))
print(cs)