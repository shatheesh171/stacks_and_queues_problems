# Design a stack which in addition to push and pop, has a function min which returns minimum element? Push, 
# pop and min should all operate at O(1)

class Node:
    def __init__(self,value=None,next=None) -> None:
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class Stack:
    def __init__(self) -> None:
        # Taking two linked list and with each push and pop updating min also
        #  so we can keep track of min
        self.items=LinkedList()
        self.minNode=LinkedList()

    def __str__(self):
        values=[str(x.value) for x in self.minNode]
        return "\n".join(values)

    def min(self):
        if self.minNode.head is None:
            return None
        return self.minNode.head.value

    def push(self,item):
        # No change in minimum node
        if self.minNode.head and (self.minNode.head.value<item):
            #print("came here",item)
            val=self.minNode.head.value
            node=Node(value=val)
            node.next=self.minNode.head
            self.minNode.head=node
        else:
            #print("came here else",item)
            node=Node(value=item)
            node.next=self.minNode.head
            self.minNode.head=node
        #Now update the other stack (top one) with value item
        node=Node(value=item)
        node.next=self.items.head
        self.items.head=node

    def pop(self):
        if not self.items.head:
            return None
        self.minNode.head=self.minNode.head.next
        item=self.items.head.value
        self.items.head=self.items.head.next
        return item



cs=Stack()
cs.push(5)
cs.push(3)
cs.push(5)
cs.push(2)
print(cs.min())
cs.pop()
cs.pop()
print(cs.min())