from cadastro import lista_produtos, id
from realizar_movimentacao import lista_movimentacao, mostrar_movimentacao

def atualizarEstoque():

  if(len(lista_produtos) > 0):
    print("Produtos cadastrados disponíveis para alteração do valor de estoque")
    lista_id = []

    for produto in lista_produtos:
      lista_id.append(produto['id_produto'])
      print(f" id: {produto['id_produto']}  - Nome Produto: {produto['nome']} - Quantidade no Estoque: {produto['quantidade']}")
  

    try:
      id_buscado = int(input("Digite o ID do produto que deseja alterar:   "))

    except ValueError:
      print("Id inválido. Digite um id válido.")
      id_buscado = -1  
    
    id_encontrado = list(filter(lambda x: x  == id_buscado, lista_id))

    if(id_encontrado == []):
      print("O do id digitado não existe ou não encontrado!") 
  
    elif(id_encontrado != []):
      tipo_movimentacao = input("Digite E para entrada ou S para a saida ")
      if(tipo_movimentacao.lower() == 'e'):
       atualizar_item('+', id_encontrado)
      elif(tipo_movimentacao.lower() == 's'):
       atualizar_item('-', id_encontrado)
  else:
    print("Não há produtos cadastrados até o momento")

def atualizar_item(operador, id_encontrado):
 
    if(operador == '-'):
      novo_estoque = int(input("Digite quantidade de itens que saiu:   "))
    elif(operador == '+'):
      novo_estoque = int(input("Digite quantidade de itens que foi adicionada ao estoque:   "))
    
    for numero in id_encontrado:
      novo_numero = numero
  
      posicao_produto = novo_numero - 1
      produto_alterado = lista_produtos[posicao_produto]
      saida_estoque = produto_alterado['quantidade'] - novo_estoque 
      entrada_estoque = produto_alterado['quantidade'] + novo_estoque 

      if(operador == '-' and saida_estoque >= 0):
          produto_alterado['quantidade'] = saida_estoque
          novo_tipo_movimentacao = 'saida'

      elif(operador == '-' and saida_estoque < 0):
          print("Estoque não pode ficar negativo")
          return False

      elif(operador == '+'):
          produto_alterado['quantidade'] = entrada_estoque  
          novo_tipo_movimentacao = 'entrada'

      t_movimentacao = produto_alterado['tipo_mov'] = novo_tipo_movimentacao
      objeto_com_estoque_atualizado = [produto_alterado['id_produto'], produto_alterado['nome'], t_movimentacao, produto_alterado['quantidade'], produto_alterado['localizacao'] ]
      
      lista_movimentacao.append(objeto_com_estoque_atualizado)
      
      print("Estoque alterado com sucesso!")

      print(f"O produto com id {produto_alterado['id_produto']} cadastrado como {produto_alterado['nome']}, teve seu valor de estoque alterado para {produto_alterado['quantidade']} ")
