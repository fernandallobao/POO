from modulo import *

if __name__ == "__main__":
  
    #construtor - instaciando o objeto da subclasse
    cc = ContaCorrente('', '', '1001-1', '10010-1', 0)

    #recebendo dados
    cc.nome = input('Informe o nome do titular: ')
    cc.cpf = input('Informe o cpf do titular: ')

    
    
    while True:
        print('\n')
        print(f'{'-'*10}Dados do Titular{'-'*10}')
        print(f'Titular da conta: {cc.nome}.')
        print(f'CPF: {cc.cpf}.')
        print(f'Agencia: {cc.agencia}.')
        print(f'Conta: {cc.conta}.')

        print('\n')
        print(f'{'-'*10}Banco Cobra{'-'*10}')
        print('1 - Saldo')
        print('2 - Depósito')
        print('3 - Saque')
        print('0 - Sair')

        op = input('Informe a ação que deseja fazer: ')

        if op == '1':
            print(f'Saldo disponivel em conta R$ {cc.saldo():,.2f}')
            continue
        elif op == '2':
            deposito = float(input('Informe o valor do depósito: ').replace(',','.'))
            if deposito > 0:
                cc.fazer_deposito(deposito)
                print(f'Depósito efetuado com sucesso!')
            else:
                print('Valor inválido')
            continue
        elif op == '3':
            saque = float(input('Informe o valor do saque: ').replace(',','.'))
            if saque <= cc.saldo
                cc.fazer_saque(saque)
                print(f'Saque efetuado no valor de R$ {saque}.')
            else:
                print('Saldo em conta insuficiente!')
            continue
        else:
            break