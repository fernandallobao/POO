class Aluno:
    #construtot
    def __init__(self, nome, matricula, cpf):
        self.__nome = nome
        self.__matricula = matricula
        self.__cpf = cpf
        self.cursos_inscritos = []

    #métodos de acesso
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    #metodos de acesso
    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self) #ligação entre ambos associação de fato

    def listar_cursos(self): # lista os cursos que o aluno foi matriculado
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome)
        return lista

class Curso:
    def __init__(self, nome, duracao, turno):
        self.__nome = nome
        self.__duracao = duracao
        self.__turno = turno
        self.alunos_inscritos = []

    #métodos de acesso

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def duracao(self):
        return self.__duracao
    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    @property
    def turno(self):
        return self.__turno
    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    #metodos de ação
    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
            aluno.inscrever_curso(self) #ligação entre ambos associação de fato

    def listar_alunos(self): #lista os alunos de um determinado curso 
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome)
            return lista

    