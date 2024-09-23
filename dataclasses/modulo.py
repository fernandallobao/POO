from dataclasses import dataclass

@dataclass #serve para forçar o py a typar os atributos antes do construtor
class Pessoa:
    #atributos
    nome: str
    idade: int
    peso: float

    