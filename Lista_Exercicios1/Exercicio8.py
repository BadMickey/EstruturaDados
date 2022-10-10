nome = input("Insira o nome do arquivo: ")

f = open(nome,'r')
file = f.readlines()
print(file)
print(" ")

x = 0
while x == 0:
    print("Existem",len(file),"linhas neste arquivo")

    lineNum = int(input('Número da linha: '))

    if lineNum <= 0 or lineNum > len(file):
        break

    print(file[lineNum-1])