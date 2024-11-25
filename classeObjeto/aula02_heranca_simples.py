class Veiculo:
    
    def __init__(self, cor, placa, numero_rodas):
        self.placa = placa
        self.cor = cor
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print('Ligando motor')
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(
                                                        [
                                                f'{chave} = {valor}' for chave, valor in self.__dict__.items()
                                                    ]
                                                        )
                                                }" 


class Motocicleta(Veiculo):
    pass
class Carro(Veiculo):
    pass
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f'{'Sim' if self.carregado == True else 'Não'} estou carregado')

"""
moto = Motocicleta("preta", "abc-1234", 2)
print(moto)
moto.ligar_motor()


carro = Carro("branco", "ter-2345", 4)
print(carro)
carro.ligar_motor()

"""
caminhao = Caminhao("roxo", "dps-6784", 8, True)
print(caminhao)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao.cor)