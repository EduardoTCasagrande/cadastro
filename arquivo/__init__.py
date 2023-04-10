def existe_arquivo(nome):
    try:
        open(nome, 'r')
        return True
    except FileNotFoundError:
        print('Arquivo criado com sucesso!')
        return False
