def reverse(lista): 
  revList = []
  for i in range((len(lista))):
    revList.append(lista[(i + 1) * -1])
  return revList 

lista = [1, 2, 3, 4, 5, 6, 7]

exec = reverse(lista)

print(exec)