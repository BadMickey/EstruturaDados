precoCompra = float(input("Insira o valor da compra para simulação de parcelamento: "))
numparcelamento = int(input("Insira o numero de parcelas que deseja: "))
PagInicial =0
saldo_atual =0
juros =0
valor_inicial =0
valor_parcela=0
parcela_juros= 0
saldo_remanecente=0

pagInicial = precoCompra * 0.1 
saldo_atual = precoCompra - pagInicial
taxaAnual = precoCompra*0.12
x = precoCompra*0.05
juros = saldo_atual *0.12/12
valor_principal = saldo_atual-juros
valor_parcela = saldo_atual / numparcelamento
parcela_juros = valor_parcela +juros
saldo_remanecente= saldo_atual - parcela_juros

print("Pagamento do mês: 1")
print("O valor do pagamento inicial: R$", pagInicial)
print("Saldo atual devido: R$", saldo_atual)
print("O valor do juros nesse mês é de: R$", juros)
print("O valor principal do mês: R$", valor_principal)
print("Pagamento do mês: R$", parcela_juros)
print("Saldo remanecente: R$", saldo_remanecente)