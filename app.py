import os

restaurante = []

def exibir_nome_do_programa():
      print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      Bem-vindo ao Sabor Express! O melhor serviço de entrega de comida da cidade.\n""")
def exibir_opcoes():   
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar restaurante')
      print('4. Sair\n')
def finalizar_app():
    os.system('cls')
    print('Obrigado por usar o Sabor Express! Até a próxima!')

def escolher_novo_restaurante():
      os.system('cls')
      print('Cadastro de novos restaurantes\n')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      restaurante.append(nome_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
      input('Digite uma tecla para voltar ao menu principal...')
      main()
      
def escolher_opcao():
    try:
      opcao_escolhida = int(input('Escolha uma opção: '))

      if opcao_escolhida == 1:
            escolher_novo_restaurante()
      elif opcao_escolhida == 2:
            print('Listar restaurante')
      elif opcao_escolhida == 3:
            print('Ativar restaurante')
      elif opcao_escolhida == 4:  # <-- Agora o 4 tem o seu lugar exclusivo!
            finalizar_app()
      else:                       # <-- O else agora só pega números errados
            opcao_invalida()
    except:
      opcao_invalida()
def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal...')
    main()




def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()