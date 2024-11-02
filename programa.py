from cadastro import *
from atualizar_estoque import *
from realizar_movimentacao import *
from localizar_produto import *

def iniciarSistema():
    cmd_saida = '/S'

    vlr_digitado = ""
    
    while(cmd_saida != vlr_digitado):
      texto = print("Digite:\n   /C => Cadastro Produtos \n   /E => Atualizar Estoque \n   /L => Mostrar a Localização \n   /R => Gerar Relatório \n   /S Sair do Sistema ")
      vlr_digitado = input()
      vlr_digitado_formatado = vlr_digitado.lower()

      if(vlr_digitado_formatado == "/c" or vlr_digitado_formatado == "c"):
        cadastrar_produto()
      
      elif(vlr_digitado.lower() == "/e" or vlr_digitado_formatado == "e"):
        atualizarEstoque()
      
      elif(vlr_digitado.lower() == "/l" or vlr_digitado_formatado == "l"):
        localizar_produtos()
      
      elif(vlr_digitado.lower() == "/r" or vlr_digitado_formatado == "r"):
        mostrar_movimentacao()
      
      elif(vlr_digitado.lower() == "/s" or vlr_digitado_formatado == "s"):
        print("Até a próxima!")

def reiniciarSistema():
  
  print("Olá novamente!")
  
  iniciarSistema()



iniciarSistema()

reiniciarSistema()
