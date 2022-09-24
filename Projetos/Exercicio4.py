def expo(base, iter):

    if iter < 0:
        print("Expoente negativo, operação inválida!")
        return False
    
    elif iter == 0:
        return 1

    elif iter % 2 == 1:
        return base * expo(base, iter-1)

    else:
        result = (expo(base, iter/2))
        return result*result

def main():
    print(expo(2,3))
    
main()