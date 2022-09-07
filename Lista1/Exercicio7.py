import statistics

lista = []

for i in range (0, 15):
    lista.append(int(input("Insira um número: ")))
    
x = statistics.median(lista)
print("A mediana é ", x)

y = statistics.mode(lista)
print("O modo é ", y)

z = statistics.mean(lista)
print("A média é ", x)