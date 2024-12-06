class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        
        
    def andar(self):
        print("Estou andando de bicicleta")
        
    def trocar_marcha(self):
        print("Estou trocando de marcha")
        
    def buzinar(self):
        print("prim prim")
        
    def parar(self):
        print("bicicleta parada")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(
                                                        [
                                                f'{chave} = {valor}' for chave, valor in self.__dict__.items()
                                                    ]
                                                        )
                                                }"   
              
caloi = Bicicleta("vermelha", "caloi", "2000", "200", "27")
print(caloi)
caloi.andar()
caloi.trocar_marcha()

