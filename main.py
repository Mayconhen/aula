from conta import conta

conta1 = conta(1, "Maycon Henrique", 1000.0, 1200.0)
valor = float(input("Digite o valor do saque: "))
print(conta.extrato(conta1))
print(conta.sacar(conta1, valor))