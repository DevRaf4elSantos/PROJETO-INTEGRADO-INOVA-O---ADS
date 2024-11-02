from realizar_movimentacao import lista_movimentacao, mostrar_movimentacao
lista_produtos = []
id = 0

def pegar_id():
  if(len(lista_produtos) == 0):
    id = 1
  elif(len(lista_produtos) != 0):
    id = len(lista_produtos) + 1
  return id


def validar_quantidade(quantidade):
    if isinstance(quantidade, int) and quantidade > 0:
        return True
    else:
        return False


def validar_preco(preco):
    if isinstance(preco, float) and preco > 0:
        return True
    else:
        return False


def validar_localizacao(localizacao):
    if localizacao.isalnum() or localizacao.isspace():
        return True
    else:
        return False


def cadastrar_produto():
  nome = input("Digite o nome do produto: ")
  categoria = input("Digite a categoria do produto: ")

  try:
    quantidade = int(input("Digite a quantidade em estoque: "))
  except ValueError:
    print("Quantidade inválida. Digite um número inteiro positivo.")
    quantidade = -1  
  while not validar_quantidade(quantidade):
    quantidade = int(input("Digite a quantidade em estoque: "))
  
  try:
    preco = float(input("Digite o preço do produto: "))
  except ValueError:
    print("Preco inválido. Digite um número real positivo.")
    quantidade = -1  
  while not validar_quantidade(quantidade):
    preco = float(input("Digite o preço do produto: "))

  try:
    localizacao = input("Digite a localização do produto no depósito: ")
  except ValueError:
    print("Localização inválida. Digite um valor válido.")
    quantidade = -1  
  while not validar_quantidade(quantidade):
    localizacao = input("Digite a localização do produto no depósito: ")
    
 
  novo_produto = {
      "id_produto": pegar_id(),
      "nome": nome,
      "tipo_mov": "entrada/cadastro",
      "categoria": categoria,
      "quantidade": quantidade,
      "preco": preco,
      "localizacao": localizacao
  }
  movimentacao = [novo_produto["id_produto"], novo_produto["nome"], novo_produto["tipo_mov"], novo_produto["quantidade"], novo_produto["localizacao"]]
  lista_movimentacao.append(movimentacao)
  lista_produtos.append(novo_produto)
 
  print("Produto Cadastrado Com Sucesso!")