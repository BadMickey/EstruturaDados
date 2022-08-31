import time

problemSize=10000000
cont=0
while problemSize>0:
    problemSize = problemSize//2
    cont+=1
    print(f'({problemSize} , {cont})')