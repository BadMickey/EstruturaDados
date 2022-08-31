from re import A


class Student:
    nome=""
    pontuacao=[]

    def __repr__(self):
        a="Nome: "+self.nome
        for i in range(len(self.pontuacao)):
            a=a+"\nPontos "+(str(i+1))+" : "+str(self.pontuacao[i])
        return a

    def __init__(self, nome, quantPontuacoes):
        self.nome=nome
        for i in range(quantPontuacoes):
           self.pontuacao.append(0)

    def puxaPontuacao(self, i):
        return self.pontuacao[(i-1)]

    def substituiPontuacao(self, i, novoPontuacao):
        self.pontuacao[i]=novoPontuacao

    def obterAsPontuacoes(self):
        return len(self.pontuacao)

    def obterPontuacaoMaisAlta(self):
        pontosOrganizados=[]
        for i in self.pontuacao:
            pontosOrganizados.append(i)

        pontosOrganizados.sort()
        return pontosOrganizados[len(pontosOrganizados)-1]

    def obterMedia(self):
        soma=0
        for i in self.pontuacao:
            soma=soma+int(i)

        return soma/len(self.pontuacao)

    def obterNomeAluno(self):
        return self.nome

    pass         

def main():
    nomeAluno=input("Digite o nome do aluno: ")
    quantPontuacoes=int(input("Digite a quantidade de pontuações: "))

    Aluno=Student(nomeAluno, quantPontuacoes)

    for i in range(quantPontuacoes):
        pontos=float(input("Digite o ponto "+str(i+1)+": "))
        Aluno.substituiPontuacao(i,pontos)
    
    a=int(input("Digite um número de pontuação para ser acessada: "))
    print("O valor dessa pontuação é: ", Aluno.puxaPontuacao(a))
    print("\nO nome do aluno é: ", Aluno.obterNomeAluno())
    print("A quantidade de pontuações é de: ", Aluno.obterAsPontuacoes())
    print("A pontuação mais alta é de: ", Aluno.obterPontuacaoMaisAlta())
    print("A média é de: ", Aluno.obterMedia())
    print("\nO objeto completo é:\n", Aluno)

    return

main()