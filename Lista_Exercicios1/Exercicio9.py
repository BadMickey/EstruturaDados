import random
import math
def main():
    print("Você deverá informar ao computador com dicas se está perto de adivinhar o número pensado por você!\n")
    print("Use > quando o número pensado for maior que o adivinhado, < quando for menor e = quando o computador acertar!\n")
    menor = int(input("Entre com o menor número: "))
    maior = int(input("Entre com o maior número: "))
    contador = 0
    limite = int(math.log(maior-menor, 2)+1)
        
    while True:
        contador+=1
        tentativaMaquina = random.randint(menor, maior)
        print(f'O número tentado foi: {tentativaMaquina}')
        dica = input("Digite a sua dica: ")
        if limite == contador:
            print("Você está trapaceando por ter acabado as tentativas!")
            break
        if dica=='=':
            print(f'Uau! Eu acertei em {contador} tentativas')
            break
        elif dica=='>':
            menor=tentativaMaquina
            print("O número pensado pelo usuário é maior que a tentativa da máquina")
        elif dica=='<':
            maior=tentativaMaquina
            print("O número pensado pelo usuário é menor que a tentativa da máquina")
            
main()