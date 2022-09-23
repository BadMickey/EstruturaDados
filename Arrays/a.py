def swap(lyst, i, j):

  temp = lyst[i]
  lyst[i] = lyst[j]
  lyst[j] = temp

def modifiedSelectionSort(reverse, lista):

    i = 0
    while i < len(lista) - 1:               
        minIndex = i                          
        j = i + 1
        while j < len(lista):                 
            if lista[j] < lista[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:                     
            swap(lista, minIndex, i)
        i += 1
    
    if reverse == True:
        revList = []
        for i in range((len(lista))):
            revList.append(lista[(i + 1) * -1])
        return revList

def main():
    sequencia = [55, 33, 1, 5, 7, 8, 12, 16, 19]

    a = modifiedSelectionSort(False, sequencia)
    
    print(sequencia)
    print(a)

main()