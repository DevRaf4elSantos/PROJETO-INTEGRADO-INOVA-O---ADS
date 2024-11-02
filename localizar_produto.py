from cadastro import lista_produtos

def localizar_produtos():
    if(len(lista_produtos) > 0):
        print('Escolha um dos produtos abaixo')
        for produto in lista_produtos:
            print(f"id: {produto['id_produto']} - produto: {produto['nome']}")
        try:
            id_buscado = int(input('Digite o id do produto que busca   '))
        except ValueError:
            print("Ocorreu um erro! Digite novamente:     ")
            id_buscado = -1
        while id_buscado == -1:
            id_buscado = int(input('Digite o id do produto que busca   '))
        if(id_buscado <= len(lista_produtos)):
            posicao = id_buscado - 1
            produto_buscado = lista_produtos[posicao]
            print(f'O produto buscado: {produto_buscado['nome']} está localizado em: {produto_buscado['localizacao']}')
        else:
            print('O id digitado não existe ou não foi encontrado!')
    else:
         print("Não há produtos cadastrados até o momento. Cadastre um novo produto!")