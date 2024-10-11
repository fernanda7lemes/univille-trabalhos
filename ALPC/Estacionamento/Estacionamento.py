import numpy as np

SETORES = ['A', 'B', 'C']
NUM_VAGAS = 5
se = 1

vagas = {setor: np.full(NUM_VAGAS, '', dtype=object) for setor in SETORES}
veiculos_estacionados = {}

def ocupar_vaga(placa):
    if placa in veiculos_estacionados:
        print(f"\nO veículo com placa {placa} já está estacionado.\n\n------------------------------------------------------------------------")
        return
    
    vagas_disponiveis = [(setor, i) for setor in SETORES for i in range(NUM_VAGAS) if vagas[setor][i] == '']
    
    if not vagas_disponiveis:
        print("\nNão há vagas disponíveis.\n\n------------------------------------------------------------------------")
        return
    
    setor, vaga = vagas_disponiveis[0]
    vagas[setor][vaga] = placa
    veiculos_estacionados[placa] = (setor, vaga)
    print(f"\nVeículo com placa {placa} estacionado no setor {setor}, vaga {vaga}.\n\n------------------------------------------------------------------------")

def liberar_vaga(placa):
    if placa not in veiculos_estacionados:
        print(f"\nO veículo com placa {placa} não está estacionado.\n\n------------------------------------------------------------------------")
        return
    
    setor, vaga = veiculos_estacionados[placa]
    vagas[setor][vaga] = ''
    del veiculos_estacionados[placa]
    print(f"\nVeículo com placa {placa} saiu da vaga no setor {setor}, vaga {vaga}.\n\n------------------------------------------------------------------------")

def exibir_vagas_disponiveis():
    print('------------------------------------------------------------------------\n                           ESTACIONAMENTO\n------------------------------------------------------------------------')
    print('Operação: Exibir vagas disponíveis\n')
    for setor in SETORES:
        vagas_livres = np.where(vagas[setor] == '', 'Disponível', 'Ocupado')
        print(f"Setor {setor}: {', '.join(vagas_livres)}")
    print('\n\n------------------------------------------------------------------------')

def consultar_veiculo(placa):
    if placa in veiculos_estacionados:
        setor, vaga = veiculos_estacionados[placa]
        print(f"O veículo com placa {placa} está estacionado no setor {setor}, vaga {vaga}.\n\n------------------------------------------------------------------------")
    else:
        print(f"O veículo com placa {placa} não está estacionado.\n\n------------------------------------------------------------------------")

def pergunta_placa(operacao):
    if operacao == 1:
        titulo = 'Operação: Estacionar carro.'
    if operacao == 3:
        titulo = 'Operação: Consultar veículo'
    if operacao == 4:
        titulo = 'Liberar vaga'
    print('------------------------------------------------------------------------\n                           ESTACIONAMENTO\n------------------------------------------------------------------------')
    print('\n',titulo)
    placa = input('\nPlaca do carro:')

    return placa

def limpar():
    print('\n'*300)

def finalizar(sessao):

    numero = 0
    
    while numero == 0:
        numero = int(input('\nDigite 1 para sair ou 0 para realizar outra operação:'))
        if numero == 1:
            sessao = 0
            limpar()
            return sessao
        elif numero == 0:
            sessao = 1
            numero = 1
            limpar()
            return sessao
        else:
            limpar()
            print('Digite um número válido!')
            numero = 0
            return numero
     
def realiza_operacao(operacao,sessao):

    if operacao == 1:
        limpar()
        placa = pergunta_placa(operacao)
        ocupar_vaga(placa)
        sair = finalizar(sessao)
        return sair
    elif operacao == 2:
        limpar()
        exibir_vagas_disponiveis()
        sair = finalizar(sessao)
        return sair
    elif operacao == 3:
        limpar()
        placa = pergunta_placa(operacao)
        consultar_veiculo(placa)
        sair = finalizar(sessao)
        return sair
    elif operacao == 4:
        limpar()
        placa = pergunta_placa(operacao)
        liberar_vaga(placa)
        sair = finalizar(sessao)
        return sair
    else:
        limpar()
        print('\nDigite uma opção válida!')
        sessao = 1
        return sessao

if __name__ == "__main__":

    while se == 1:

        print('------------------------------------------------------------------------\n                           ESTACIONAMENTO\n------------------------------------------------------------------------')
        print('\n\n1 - Estacionar carro\n2 - Exibir vagas disponíveis\n3 - Consultar veículo\n4 - Liberar vaga\n')
        op = int(input('\nDigite o número correspondente a operação que você deseja realizar:'))
        se = realiza_operacao(op,se)

    print('Finalizando...')