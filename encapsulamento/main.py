from classe import *

if __name__ == '__main__':
    #entrada de dados
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    email = input('Informe o e-mail: ')

    #instancia da classe
    usuario = Pessoa(nome, idade, email)

    #saíde de dados
    print(f'Nome: {usuario.nome}')
    print(f'Idade: {usuario.idade}')
    print(f'E-mail: {usuario.email}')