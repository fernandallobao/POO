# NOTE: cria a classe
class Pessoa:
    #os atributos são sempre definidos dentro do método constrtutor
    #NOTE: método construtor
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

    
if __name__ == '__main__':
    #entrada de dados
    nome = input('Informe o nome do usuário: ')
    idade = int(input('Informe a idade do usuário: '))
    cpf = input('Informe o cpf do usuário: ')
    email = input('Informe o email do usuário: ')

    #instanciando o objeto
    usuario = Pessoa(nome, idade, cpf, email)

    #saida de dados
    print(f'Nome: {usuario.nome}')
    print(f'Idade: {usuario.idade}')
    print(f'CPF: {usuario.cpf}')
    print(f'E-mail: {usuario.email}')