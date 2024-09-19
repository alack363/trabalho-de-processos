# Classe filha
from bomba_combustivel import BombaCombustivel

class BombaGasolina(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(self, valor_litro, quantidade_disponivel)

    def abastecer_por_valor_com_aditivo(self, valor):
        preco_aditivo = super().get_preco() * 1.05
        litros = valor / preco_aditivo
        return litros
    
    def abastecer_por_litro_com_aditivo(self, litros):
        preco_aditivo = litros * 1,05
        litros = valor * preco_aditivo
        valor = litros * super().get_preco()
        return valor


# Testing
bomba = BombaGasolina(2, 100)
pagar = BombaGasolina.abastecer_por_valor(100)
print(pagar)

quantidade = BombaGasolina.get_quantidade_disponivel_no_tanque()
print(quantidade)