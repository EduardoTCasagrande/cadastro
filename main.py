import lib
import arquivo
from time import sleep

if arquivo.existe_arquivo('banco.txt'):
    arquivo = open('banco.txt', 'r')
else:
    arquivo = open('banco.txt', 'w')
while True:
    lib.cabecalho('MENU PRINCIPAL'.center(40))
    lib.menu()
    opcao = lib.leiaint('Digite uma opção: ')
    if opcao == 1:
        with open('banco.txt', 'r') as arquivo:
            lib.cabecalho('\033[35mOPÇÃO 1\033[m'.center(47))
            print(arquivo.read())
    elif opcao == 2:
        with open('banco.txt', 'a') as arquivo:
            lib.cabecalho('\033[35mOPÇÃO 2\033[m'.center(47))
            pessoa = {'nome': str(input('Digite seu nome: ').title())}
            idade = lib.leiaint('Digite sua idade: ')
            pessoa['idade'] = idade
            arquivo.write(f'Nome: {pessoa["nome"]}, Idade: {pessoa["idade"]}\n')
    elif opcao == 3:
        nome = str(input('Digite o nome para deletar os dados: ')).title()
        del_pessoa = []
        encontrou_pessoa = False
        with open('banco.txt', 'r') as arquivo:
            for linha in arquivo:
                if nome.strip() in linha:
                    encontrou_pessoa = True
                else:
                    del_pessoa.append(linha)
        if encontrou_pessoa:
            with open('banco.txt', 'w') as arquivo:
                arquivo.writelines(del_pessoa)
        else:
            print('Erro. ninguem com esse nome no sistema')
    elif opcao == 5:
        break
    else:
        print(lib.erro(2))
    sleep(1)
print('<<  VOLTE SEMPRE  >>')
