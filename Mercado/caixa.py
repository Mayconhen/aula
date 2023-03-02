from produto import produto
from carteira import carteira

produto1 = produto("Leite", "Desnatado", 100.0, 5)
produto2 = produto("Biscoito", "chocolate", 50.0, 5)
carteira1= carteira(100000.0)

carteira.comprar(carteira1, produto2.valor)
carteira.comprar(carteira1, produto1.valor)
carteira.comprar(carteira1, produto2.valor)
carteira.comprar(carteira1, produto1.valor)
carteira1.saldototal