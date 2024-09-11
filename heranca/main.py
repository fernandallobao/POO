#superclasse (classe-mãe)
class Pessoa:
    #atributos
    cidade = 'Brasília'
    telefone = '(61) 98765-4321'
    email = 'fulaninho@gmail.com'

# subclasse (classe-filha)
class PessoaFisica(Pessoa):
    #atributos
    nome = 'fulano de Tal'
    cpf = '12345689'
    peso = 90
    altura = 1.60

# subclasse (classe-filha)
class PessoaJuridica(Pessoa):
    #atributos
    nome_fantasia = 'Jailto programações'
    razao_social = 'Jailton Cascavel Ltda'
    cnpj = '12345689/0001-65'
    

#programa principal
if __name__ == '__main__':
    #instancia dos objetos
    usuario = PessoaFisica()
    empresa = PessoaJuridica()

    print(f'{'-'*30} DADOS DO USUARIO {'-'*30}')
    print(f'Nome do usuário: {usuario.nome}')
    print(f'CPF do usuário: {usuario.cpf}')
    print(f'Peso do usuário: {usuario.peso}')
    print(f'Altura do usuário: {usuario.altura}')
    print(f'Cidade do usuário: {usuario.cidade}')
    print(f'Telefone do usuário: {usuario.telefone}')
    print(f'E-mail do usuário: {usuario.email}')

    print('\n')

    print(f'{'-'*30} DADOS DA EMPRESA {'-'*30}')
    print(f'Nome da empresa: {empresa.nome_fantasia}')
    print(f'Razão social da empresa: {empresa.razao_social}')
    print(f'CNPJ da empresa: {empresa.cnpj}')
    print(f'Cidade da empresa: {empresa.cidade}')
    print(f'Telefone da empresa: {empresa.telefone}')
    print(f'E-mail da empresa: {empresa.email}')
    

