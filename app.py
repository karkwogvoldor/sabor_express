import os

restaurantes = ['Sabor Caseiro', 'Jorje Sushi', 'Pizzaria do Zé']

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
    exibir_subtitulo('Finalizando o App...')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal...')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def escolher_novo_restaurante():
      exibir_subtitulo('Cadastro de novo restaurante')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      restaurantes.append(nome_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
      voltar_ao_menu_principal()

def listar_restaurantes():
      exibir_subtitulo('Lista de restaurantes cadastrados')
      for restaurante in restaurantes:
            print(f'- {restaurante}')
      voltar_ao_menu_principal()

def escolher_opcao():
    try:
      opcao_escolhida = int(input('Escolha uma opção: '))

      if opcao_escolhida == 1:
            escolher_novo_restaurante()
      elif opcao_escolhida == 2:
            listar_restaurantes()
      elif opcao_escolhida == 3:
            print('Ativar restaurante')
      elif opcao_escolhida == 4:  # <-- Agora o 4 tem o seu lugar exclusivo!
            finalizar_app()
      else:                       # <-- O else agora só pega números errados
            opcao_invalida()
    except:
      opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()