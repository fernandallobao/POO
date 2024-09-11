#POLIMORFISMO
#superclasse, classe-mãe, classe base
class Pessoa:
    #MÉTODO CONTRUTOR DA CLASSE PESSOA - atributos
    def __init__(self, endereco, email, telefone): #sempre colocar self antes para direferencia-lo de função
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

    #metodo
    def mostrar_cartao_visitas(self):
        print(f'Endereço: {self.endereco}')
        print(f'E-mail: {self.email}')
        print(f'Telefone: {self.telefone}')


#subclasse, classe-filha, clasee derivada Pessoa Física
class PessoaFisica(Pessoa):
    #Polimorfismo do metodo contrutor
    def __init__(self, nome, cpf, profissao, endereco, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        #para ele entender a mudança de comportamento - super para ele pegar o restante da superclass
        super().__init__(endereco, email, telefone)

    def mostrar_cartao_visitas(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Profissao: {self.profissao}')
        #para ele entender a mudança de comportamento - super para ele pegar o restante da superclass
        super().mostrar_cartao_visitas()

#subclasse, classe-filha, clasee derivada Pessoa Física
class PessoaJuridica(Pessoa):
    #Polimorfismo do metodo contrutor
    def __init__(self, nome_fantasia, razao_social, cnpj, endereco, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.cnpj = cnpj
        #para ele entender a mudança de comportamento - super para ele pegar o restante da superclass
        super().__init__(endereco, email, telefone)

    def mostrar_cartao_visitas(self):
        print(f'Nome fantasia: {self.nome_fantasia}')
        print(f'Razão social: {self.razao_social}')
        print(f'CNPJ: {self.cnpj}')
        #para ele entender a mudança de comportamento - super para ele pegar o restante da superclass
        super().mostrar_cartao_visitas()
