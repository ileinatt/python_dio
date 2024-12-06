# TODO: Crie uma classe e método para realizar a soma:
class Calculadora():
    def soma(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        return self.numero_1+ self.numero_2



num1 = int(input())
num2 = int(input())


# Criando uma instância da calculadora
calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)