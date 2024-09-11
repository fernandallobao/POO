import classes as cl

if __name__ == '__main__':
    #entrada de dados
    nome = input('Informe o nome do usuário: ')
    cpf = input('Informe o cpf do usuário: ')
    profissao = input('Informe a profissao do usuário: ')
    endereco = input('Informe o endereco do usuário: ')
    email = input('Informe o email do usuário: ')
    telefone = input('Informe o telefone do usuário: ')

    # instanciando as classes
    usuario = cl.PessoaFisica(nome, cpf, profissao, endereco, email, telefone)

    #entrada de dados
    nome = input('Informe o nome da empresa: ')
    razao_social = input('Informe o nome da razao_social da empresa: ')
    cnpj = input('Informe o CNPJ da empresa: ')
    endereco = input('Informe o endereco da empresa: ')
    email = input('Informe o email da empresa: ')
    telefone = input('Informe o telefone da empresa: ')

    empresa = cl.PessoaJuridica(nome, razao_social, cnpj, endereco, email, telefone)

    #saida de dados
    print('\n')
    usuario.mostrar_cartao_visitas()
    print('-'*30)
    empresa.mostrar_cartao_visitas()