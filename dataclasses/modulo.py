from dataclasses import dataclass

@dataclass #serve para forçar o py a typar os atributos antes do construtor. ja deixa os atributos privados e ja faz os get e set
class Pessoa:
    #atributos
    nome: str
    idade: int
    peso: float

    def __str__(self):
        return f'Meu nome é {self.nome}, tenho {self.idade}, peso {self.peso}kg.'