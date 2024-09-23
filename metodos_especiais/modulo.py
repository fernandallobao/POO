class Pessoa:
    #metodo contrutror
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    #outros metodos especiais

    #__str__ retorna respresentação de valores que sejam legiveis para as pessoas
    def __str__(self): 
        return f'Meu nom é {self.nome}, {self.idade} anos, meu email {self.email}'

    # repr() gera representações que o interpretador PY consegue ler(ou levantar uma exceção SyntaxError, se não houver sintaxe equivalente). Alternativa try except
    def __repr__(self):
        return f'Pessoa({self.nome}, {self.idade}, {self.email})'
    
    # len informa o tamanho de um determinado objeto
    def __len__(self):
        return self.nome
    
    # del metodo destutor, detroi objeto. Limpeza de memoria, pouco usado
    def __del__(self):
        print( f'O objeto {self.idade}, foi eliminado')