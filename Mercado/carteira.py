from produto import produto

class carteira:

    def __init__(self, saldo):
        print("Carteira adicionada")
        self.__saldo = saldo

    def comprar(self, valor):
        print("comprando...")
        self.__saldo -= valor
    
    @property
    def saldototal(self):
        print("Saldo total:{}".format(self.__saldo))
        