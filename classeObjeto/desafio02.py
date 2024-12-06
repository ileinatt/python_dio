class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#TODO: Crie um método para retornar as informações formatas com Nome e Idade:    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(
                                                        [
                                                f'{chave} = {valor}' for chave, valor in self.__dict__.items()
                                                    ]
                                                        )
                                                }" 

# Entrada do usuário
nome = input()
idade = int(input())

# TODO: Crie uma instância da pessoa:

cadastro = Pessoa(nome, idade)

#TODO: Chame o método para retornar as informações formatadas e imprima o resultado:

print(cadastro)