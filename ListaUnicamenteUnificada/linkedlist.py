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
    
    def _getnode(self, index):
        probe = self.head
        for i in range(index):
            if probe:
                probe = probe.next
            else:
                raise IndexError("List index out of range")
        return probe    
    
    def __getitem__(self, index):
        probe = self._getnode(index)
        if probe:
            return probe.data
        else:
            raise IndexError("List index out of range")
    
    def __setitem__(self, index, item):
        probe = self._getnode(index)
        if probe:
            probe.data = item
        else: 
            raise IndexError("List index out of range")
    
    def index(self, item):
        probe = self.head
        i = 0
        while(probe):
            if probe.data == item:
                return i
            probe = probe.next
            i+=1
        raise ValueError("{} is not int list".format(item))

    def __repr__(self) -> str:
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"         
            pointer = pointer.next
        return r

    def __str__(self) -> str:
        return self.__repr__()

lista = LinkedList()
# inserindo na última posição
lista.append(5)
lista.append(10) 
# retorna o tamanho da lista
print(f'O tamanho da lista é: {lista._size}')   
# retorna o item baseado no indice
print(f'O valor no indice 0 é: {lista.__getitem__(0)}')
print(f'O valor no indice 1 é: {lista.__getitem__(1)}')
# substitui um item baseado no indice      
lista[0] = 10
lista[1] = 20
# retorna o indice de um valor    
print(f'O valor 10 está no indice: {lista.index(10)}')
print(f'O valor 20 está no indice: {lista.index(20)}')
# imprime a lista
print(lista)
