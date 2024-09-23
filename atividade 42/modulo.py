# Crie um programa de locação de veículo, que receba o cadastro de um usuário para que ele possa escolher entre 5 veículos previamente cadastrados no sistema, e no final o programa exibe os dados do cliente e do carro que ele decidiu alugar.
# O algoritmo deve ser criado com base no conceito de Associação entre Classes visto na aula do dia 18/09/2024.

class Cliente:
    def __init__(self, nome, cpf, idade, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__telefone = telefone
        self.carros_alugados = []

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def aluga_carro(self, carro):
        if carro not in self.carros_alugados:
            self.carros_alugados.append(carro)
            carro.adicionar_carro(self)

    def listar_carros(self):
        lista = []
        for carro in self.carros_alugados:
            lista.append(carro.modelo)
        return lista

    
class Carro:
    def __init__(self, modelo, cor, ano, preco):
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano
        self.__preco = preco
        self.cliente_do_carro = []

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def _cor(self, cor):
        self.__cor = cor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco


    #metodos de ação
    def adicionar_carro(self, cliente):
        if cliente not in self.cliente_do_carro:
            self.cliente_do_carro.append(cliente)
            cliente.aluga_carro(self)

    def listar_clientes(self):
        lista = []
        for cliente in self.cliente_do_carro:
            lista.append(cliente.nome)
            return lista