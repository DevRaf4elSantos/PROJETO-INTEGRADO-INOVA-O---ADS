lista_movimentacao = []

def mostrar_movimentacao():
    if(len(lista_movimentacao) > 0):
        print('Relação da movimentação do(s) produto(s):')
        for movimentacao in lista_movimentacao:
            print(f"id: {movimentacao[0]} - produto: {movimentacao[1]} - tipo movimentção: {movimentacao[2]} - quantidade: {movimentacao[3]} - localizado em: {movimentacao[4]} ")
    else:
        print("Não houve movimentações até o momento. Cadastre um novo produto!")
