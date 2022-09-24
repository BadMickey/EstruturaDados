def reverse(lista): 
  reverseList = []
  for i in range((len(lista))):
    reverseList.append(lista[(i + 1) * -1])
  return reverseList 

lista = [1, 2, 3, 4, 5, 6, 7]

def main():

  resultado = reverse(lista)

  print(resultado)
  
main()