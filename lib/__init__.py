def linha(tamanho=40):
    print('-' * tamanho)

def cabecalho(txt=''):
    linha()
    print(txt)
    linha()

def menu():
    print('\033[36m1\033[m- \033[35mVer Pessoas Cadastradas\033[m')
    print('\033[36m2\033[m- \033[35mCadastrar Pessoa\033[m')
    print('\033[36m3\033[m- \033[35mDeletar Pessoa\033[m')
    print('\033[36m4\033[m- \033[35mAlterar Dados\033[m')
    print('\033[36m5\033[m- \033[35mSair do Sistema\033[m')

def erro(opc=0):
    erros = ['\033[0;31mERRO: APENAS NÚMEROS INTEIROS.\033[m',
             '\n\033[0;31mUsuario preferiu interromper o programa.\033[m',
             '\033[0;31mERRO: OPÇÃO INVALIDA. TENTE NOVAMENTE.\033[m']
    return erros[opc]

def leiaint(msg=''):
    while True:
        try:
            opc = int(input(msg))
            break
        except ValueError:
            print(erro(0))
        except KeyboardInterrupt:
            print(erro(1))
    return opc
