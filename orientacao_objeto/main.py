# NOTE: criar classe
class Carro:
    #atributos - características
    fabricante = 'Volkswagen'
    modelo = 'Gol'
    ano = '2011'
    cor = 'preto'
    placa ='GTA42B8'

    #metodo - ações
    def ligar(self, ignicao):
        if ignicao:
            return f'{self.modelo} está ligado!'
        else:
            return f'{self.modelo} está desligado!'
        
    
# NOTE: programa principal

if __name__ == '__main__': #protege o programa principal 
    #instanciando a claase carro (cria objeto)
    meu_carro = Carro()

    #exibir os atributos do objeto
    print(f'Fabricante: {meu_carro.fabricante}')
    print(f'Modelo: {meu_carro.modelo}')
    print(f'Ano: {meu_carro.ano}')
    print(f'Cor: {meu_carro.cor}')
    print(f'Placa: {meu_carro.placa}')

    #ligar (ou não) o carro
    ligar_carro = True

    #chama o metodo do objeto
    print(meu_carro.ligar(ligar_carro))

