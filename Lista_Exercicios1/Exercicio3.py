def Exercicio():
    
    altura_inicial = float(input("Insira a altura inicial: "))
    quant_quicadas = float(input("Insira a quantidade de quicadas: "))
    indice_de_quicamento = quant_quicadas/altura_inicial
    altura = altura_inicial
    altura_total = altura_inicial
    print(f"Índice de quicada: {indice_de_quicamento:.2f}")

    while(quant_quicadas > 0):
        altura = indice_de_quicamento * altura
        altura_total = altura_total + (2*altura)
        quant_quicadas = quant_quicadas -1
        if(quant_quicadas == 0):
            print(f"A distância total percorrida é de {altura_total:.2f} m")
            break
        
Exercicio()