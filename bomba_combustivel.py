class BombaCombustivel:
    
  def __init__(self, valor_litro, quantidade_disponivel,):
    self.__valor_litro = valor_litro
    self.__quantidade_disponivel = quantidade_disponivel 

  def abastecer_por_valor(self, valor):
    litros = valor / self.__valor_litro
    erro = self.quantidade_disponivel_no_tanque(litros)
    if erro == -1:
       return erro
    return litros

  def abastecer_por_litro(self, litros):
    valor = litros * self.__valor_litro
    erro = self.quantidade_disponivel_no_tanque(litros)
    if erro == -1:
       return erro
    return valor
  
  def quantidade_disponivel_no_tanque(self, litros_a_retirar):
        if litros_a_retirar < 0:
            return -1
        
        nova_quantidade = self.__quantidade_disponivel - litros_a_retirar
        
        if nova_quantidade < 0:
            return -1
        
        self.__quantidade_disponivel = nova_quantidade  # Atualiza o valor de __quantidade_disponivel
        return self.__quantidade_disponivel

  def get_quantidade_disponivel_no_tanque(self):
     return self.__quantidade_disponivel
  
  def get_preco(self):
     return self.__valor_litro  

# # Testing
# bomba = BombaCombustivel(2, 100)
# pagar = bomba.abastecer_por_valor(100)
# print(pagar)

# quantidade = bomba.get_quantidade_disponivel_no_tanque()
# print(quantidade)