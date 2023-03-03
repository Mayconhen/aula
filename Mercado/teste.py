class veiculo:

    def __init__(self, nome, marca, lugares):
        self._nome = nome
        self._marca = marca
        self._lugares = lugares

class carro(veiculo):
    def __init__(self, nome, marca, lugares, tipo):
        super().__init__(nome, marca, lugares)
        print("Criando carro...")
        self._tipo = tipo
        

class caminhonete(veiculo):
    def __init__(self, nome, marca, lugares, capacidadecacamba):
        super().__init__(nome, marca, lugares)
        print("Criando caminhonete...")
        self._capacidadecacamba = capacidadecacamba


carro1 = carro("Veloster", "Hyundai", 5, "Sedan")
caminhonete1= caminhonete("Hilux", "Toyota", 7, 1000.0)


