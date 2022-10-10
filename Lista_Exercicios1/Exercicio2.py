salarioHora = float(input("Digite o salario por hora: "))
totalHorasReg = float(input("Digite o total de horas regulares: "))
totalHorasExt = float(input("Digite o total de horas extras: "))
pagHorasExt = totalHorasExt * (1.5 * salarioHora)

print("O pagamento semanal total é: ", salarioHora * totalHorasReg + pagHorasExt * 5)