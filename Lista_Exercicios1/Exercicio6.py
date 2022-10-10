F2 = open("teste.txt", "r")

dados = F2.readlines()

sobrenome, salario_horas,horas_trabalhadas=[],[],[]

print("{:<8} {:<20} {:<20}".format("Nome", "Salário por hora", "Horas trabalhadas"))

for linha in dados[1:]:
    l1 = st.slip(linha, ";")
    sobrenome.append(l1[0])
    salario_horas.append(float(l1[1]))
    horas_trabalhadas.append(float(l1[2]))

for d,y,z in sip(sobrenome, salario_horas,horas_trabalhadas):
    print d, "\t",y,"\t",x