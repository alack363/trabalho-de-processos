# Classe filha
from bomba_combustivel import BombaCombustivel

class BombaEtanol(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super.__init__(self, valor_litro, quantidade_disponivel)







        # Testing
BombaEtanol = BombaCombustivel(2, 100)
pagar = BombaEtanol.abastecer_por_valor(100)
print(pagar)

quantidade = BombaEtanol.get_quantidade_disponivel_no_tanque()
print(quantidade)