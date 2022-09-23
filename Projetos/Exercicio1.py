def pesquisa(lista, targ):
  for i in range(len(lista)):
    if lista[i] == targ:
      return i
  return False

lista = [3, 14, 36, 24, 51, 65]
targ = 51

indi = pesquisa(lista, targ)
if indi is not False:
  print("O índice do número ", targ, " é ", indi)
else:
  print("Não está na lista")

# O MELHOR CASO É DE O(1), PRIMEIRA POSIÇÃO DA LISTA;
# O CASO MÉDIO, POR DESCONSIDERAR CONSTANTES E VALORES QUE MULTIPLICAM N ACABA POR SER O(n);
# O PIOR CASO É O(n), ESTÁ NA ÚLTIMA POSIÇÃO DA LISTA OU NEM MESMO ESTÁ NA LISTA.