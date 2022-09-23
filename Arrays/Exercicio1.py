class Array(object):
    """Representa um array."""
    def __init__(self, capacity, fillValue=0):
        """Capacidade é o tamanho estático do array.
        fillValue é colocado em cada posição."""
        self.items = list()
        self.logicalSize=0
        for count in range(capacity):
            self.items.append(fillValue)
        
    def __len__(self):
        """-> A capacidade do array."""
        return len(self.items)
    
    def size(self):
            return self.logicalSize(self.items)

    def __str__(self):
        """-> A representação de string do array."""
        return str(self.items)

    def __iter__(self):
        """Suporta o percurso com um laço for."""
        return iter(self.items)

    def __getitem__(self, index):
        """Operador de subscrito para acesso no índice."""
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Operador de subscrito para substituição no índice."""
        if index < 0 or index > self.__sizeof__():
            print('Nao adicionado')
            if self.items[index] != newItem:
                self.logicalSize += 1
                print('Numero diferente')
            else:
                print('numero igual')
        else:
            print("")
        self.items[index] = newItem
    
def main():

    teste = Array(10)
    teste[5] = 1
    teste[6] = 1
    teste[5] = 1
    print(teste)
    print(Array.size)

main()
