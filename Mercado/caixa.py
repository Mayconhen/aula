from produto import produto
from carteira import carteira


produto1 = produto("Leite", "Desnatado", 100.0, 5)
produto2 = produto("Biscoito", "chocolate", 50.0, 5)
produto3 = produto("Arroz", "Branco", 80, 1)
carteira1= carteira(100000.0)

carteira.comprar(carteira1, produto2.valor)

x = produto1.unidade + produto2.unidade + produto3.unidade

print(x)