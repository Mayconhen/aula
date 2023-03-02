from produto import produto
from carteira import carteira

produto1 = produto("Leite", "Desnatado", 100.0, 5)
produto2 = produto("Biscoito", "chocolate", 50.0, 5)

print(produto.__radd__(produto, produto))