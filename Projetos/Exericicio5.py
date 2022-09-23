def swap(lyst, i, j):

  temp = lyst[i]
  lyst[i] = lyst[j]
  lyst[j] = temp

def modifiedSelectionSort(reverse, lista):
  
    if reverse == False:
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
        return lista

    elif reverse == True:
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

    revList = []
    for i in range((len(lista))):
      revList.append(lista[(i + 1) * -1])
    return revList

def main():
    sequencia = [55, 33, 1, 5, 7, 8, 12, 16, 19]

    a = modifiedSelectionSort(False, sequencia)
    print("sdlgvsd")

main()