print("O matemático alemão Gottfried Leibniz desenvolveu o seguinte método para aproximar o valor de pi : 𝛑/4 = 1 - 1/3 + 1/5 - 1/7 + … ")
print("Após cada divisão(interação) feita aumenta um numero após a virgula. Vamos testar!!")
interacoes = int(input("Insira o número de interações entre: "))
p=0
denominador=1
numerador=1
for i in range(interacoes):
    p=p+(numerador/denominador)
    denominador=denominador+2 
    numerador=numerador*(-1)

pi=p*4 

print("O valor de pi é: ",pi)