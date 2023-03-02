class conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando conta...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite 
        
    def extrato(self):
        print("O saldo de {} é de {} com o limite de{}".format(self.__titular, self.__saldo, self.__limite))

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor

    def deposita(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)

    @staticmethod
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def get_limite(self):
        return self.__limite
    
    @property
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
        