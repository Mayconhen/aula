class produto:

    def __init__(self, nome, descricao, valor, unidade):
        print("Criando produto...")
        print("Adicionado ao carrinho...")
        self._nome = nome
        self._descricao = descricao
        self._valor = valor
        self._unidade = unidade
        

    def __radd__(self, other):
        if isinstance(other, produto):
            return self._unidade + other._unidade
        else:
            return self._unidade + other

    @property
    def produto(self):
        print("\nProduto:{}\nDescrição:{}\nValor:{}\n".format(self.__nome, self.__descricao, self.__valor))

    @property
    def nome(self):
        return self.nome

    @property
    def descricao(self):
        return self._descricao

    @property
    def valor(self):
        return self._valor
    
    @property
    def unidade(self):
        return self._unidade
    
        
    
