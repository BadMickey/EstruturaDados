from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    def _len_(self):
        return self._size

    def __repr__(self) -> str:
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self) -> str:
        return self.__repr__()

    def __contains__(self, item):
        if(self.isEmpty()== True):
            raise IndexError("The Stack is Empty")
        
        probe = self.top
        while probe:
            if(probe.data==item):
                return True
            probe=probe.next
        
        return False

    def isEmpty(self):
        if self.top:
            return False

pilha = Stack()
pilha.push(1)
pilha.push(3)
print(pilha)
print(pilha.__contains__(2))