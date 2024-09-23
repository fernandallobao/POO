from modulo import *

if __name__ == '__main__': #impede a importação dos dados do arquivo app
    usuario = Pessoa('',0,'')

    usuario.nome = input('Informe o nome: ')
    usuario.idade = int(input('Informe a idade: '))
    usuario.email = input('Informe o e-mail: ')

    #saida de dados
    print(str(usuario))
    print(repr(usuario))
