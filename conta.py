class conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando conta...")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite 
        
    def extrato(self):
        print("O saldo de {} é de {}".format(self.titular, self.saldo))

    def sacar(self, valor):
        print("O saque total foi de {}".format(self.saldo - valor))