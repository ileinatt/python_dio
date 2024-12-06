#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class Conversor():
    def celsius_para_fahrenheit(self, celsius):
        self.celcius = celsius
        return (self.celcius * (9/5)) + 32

# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:

conversor = Conversor()


fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)