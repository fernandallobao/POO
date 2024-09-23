from modulo import *

if __name__ == '__main__':
    usuario = Pessoa('',0,0.0)

    usuario.nome = input('informe o nome: ')
    usuario.idade = input('informe a idade: ')
    usuario.peso = input('informe o peso: ')

    print(str(usuario))