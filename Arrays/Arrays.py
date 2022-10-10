"""
Exercicios feitos nesse arquivo:
1. Adicione uma variável de instância logicalSize à classe Array. Essa variável é inicialmente 0 e rastreará o número de itens atualmente disponíveis para os usuários do array. 
Em seguida, adicione o método size() à classe Array. Esse método deve retornar o tamanho lógico do array. O método __len__ ainda deve retornar a capacidade ou tamanho físico do
array.

2. Adicione precondições aos métodos __getitem__ e __setitem__ da classe Array. A pré-condição de cada método é 0 <= index < size(). Certifique-se de disparar uma exceção se a 
precondição não for atendida.
"""
class Array(object):
    """Representa um array."""
    def __init__(self, capacity, fillValue=None):
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
        "return self.logicalSize(self.items)"

    def __str__(self):
        """-> A representação de string do array."""
        return str(self.items)

    def __iter__(self):
        """Suporta o percurso com um laço for."""
        return iter(self.items)

    def __getitem__(self, index):
        """Operador de subscrito para acesso no índice."""
        if index > 0 or index < self.size():
            return self.items[index]

    def __setitem__(self, index, newItem):
        """Operador de subscrito para substituição no índice."""
        if index < 0 or index > self.size():
            print('Nao adicionado')
        else:
            if self.items[index] != newItem:    
                self.logicalSize+=1
                print('Numero diferente')
            else:
                print('numero igual')
            print("Adicionado")
            self.items[index] = newItem
    
def main():

    teste = Array(10)
    teste[5] = 1
    teste[6] = 1
    teste[5] = 1
    print(teste)
    print(Array.__sizeof__)

main()
