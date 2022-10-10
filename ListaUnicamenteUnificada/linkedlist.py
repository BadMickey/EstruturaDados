import re
from node import Node
""" linkedlist.py 
Cria Classe LinkeList que será responsável pela criação implementação das operações da lista encadeada """
class LinkedList(object):
    def __init__(self):
        self.head = None
        self._size = 0
    def append(self,newItem):
        if self.head:
            # inserção quando a lista já possui itens
            probe = self.head
            while (probe.next):
                probe = probe.next
            probe.next = Node(newItem)
        else:
            # primeira inserção
            self.head = Node(newItem)
        self._size += 1

    def __len__(self):
        return self._size

    def __repr__(self) -> str:
        return f'LinkedList(head={self.head}, size={self._size})'
        """r = ""
        pointer = self.head
        while(pointer.next):
            r = r + str(pointer.data) + " "
            pointer = pointer.next
        return r"""

    def __str__(self) -> str:
        return self.__repr__()

a = LinkedList()
a.append(5)
print(len(a))
print()