class produto:

    def __init__(self, nome, descricao, valor, unidade):
        print("Criando produto...")
        print("Adicionado ao carrinho...")
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        self.__unidade = unidade
        

    def __radd__(self, other):
        if isinstance(other, produto):
            return self.__unidade + other.__unidade
        else:
            return self.__unidade + other

    @property
    def produto(self):
        print("\nProduto:{}\nDescrição:{}\nValor:{}\n".format(self.__nome, self.__descricao, self.__valor))

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor
    
        
    
