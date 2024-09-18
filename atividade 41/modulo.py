# Crie um programa de locação de veículo, que receba o cadastro de um usuário para que ele possa escolher entre 5 veículos previamente cadastrados no sistema, e no final o programa exibe os dados do cliente e do carro que ele decidiu alugar.
# O algoritmo deve ser criado com base no conceito de Associação entre Classes visto na aula do dia 18/09/2024.

class Cliente:
    def __init__(self, nome, cpf, idade, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__telefone = telefone

    @property
    def _nome(self):
        return self.__nome
    @_nome.setter
    def _nome(self, nome):
        self.__nome = nome

    @property
    def _cpf(self):
        return self.__cpf
    @_cpf.setter
    def _cpf(self, cpf):
        self.__cpf = cpf

    @property
    def _idade(self):
        return self.__idade
    @_idade.setter
    def _idade(self, idade):
        self.__idade = idade

    @property
    def _telefone(self):
        return self.__telefone
    @_telefone.setter
    def _telefone(self, telefone):
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

    @property
    def _modelo(self):
        return self.__modelo

    @_modelo.setter
    def _modelo(self, modelo):
        self.__modelo = modelo

    @property
    def _cor(self):
        return self.__cor

    @_cor.setter
    def _cor(self, cor):
        self.__cor = cor

    @property
    def _ano(self):
        return self.__ano

    @_ano.setter
    def _ano(self, ano):
        self.__ano = ano

    @property
    def _preco(self):
        return self.__preco

    @_preco.setter
    def _preco(self, preco):
        self.__preco = preco


    