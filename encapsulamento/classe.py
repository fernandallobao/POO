class Pessoa:
    #metodo construtor
    # def __init__(self, nome, idade, email):
    #     self.nome = nome     #public
    #     self._idade = idade  #protected - visivel para subclasses que tenham relação com ela
    #     self.__email = email #private - visivel apenas dentro da sua classe, mas pode ser herdado

    def __init__(self, nome, idade, email):
        self.__nome = nome  
        self.__idade = idade 
        self.__email = email

    #metodos de acesso

    # forma errada de fazer no python
    # def get_nome(self): #pega o valor do atributo
    #     return self.__nome
    # def set_nome(self, nome): #coloca o valor no atributo
    #     self.__nome = nome

    # def get_idade(self): #pega o valor do atributo
    #     return self.__idade
    # def set_idade(self, idade): #coloca o valor no atributo
    #     self.__idade = idade

    # def get_email(self): #pega o valor do atributo
    #     return self.__email
    # def set_email(self, email): #coloca o valor no atributo
    #     self.__email = email

    #método get nome
    @property
    def nome(self):
        return self.__nome
    #método set nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    #------------------------------------
    #método get idade
    @property
    def idade(self):
        return self.__idade
    #método set idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    #------------------------------------
    #método get email
    @property
    def email(self):
        return self.__email
    #método set email
    @email.setter
    def email(self, email):
        self.__email = email