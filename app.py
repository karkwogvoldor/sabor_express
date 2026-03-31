import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
            {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
            {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
      '''Função para exibir o nome do programa. Imprime um banner de boas-vindas com o nome do programa e uma breve descrição.'''
      print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      Bem-vindo ao Sabor Express! O melhor serviço de entrega de comida da cidade.\n''')

def exibir_opcoes():
      '''Função para exibir as opções do menu. Imprime as opções disponíveis para o usuário escolher, incluindo cadastrar restaurante, listar restaurantes, ativar/desativar restaurante e sair do programa.'''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar/Desativar restaurante')
      print('4. Sair\n')

def finalizar_app():
      '''Função para finalizar o aplicativo. Exibe uma mensagem de despedida e encerra o programa.'''
      exibir_subtitulo('Finalizando o App...')

def voltar_ao_menu_principal():
      '''Função para voltar ao menu principal. Solicita ao usuário que pressione uma tecla para retornar ao menu principal e chama a função main() para exibir o menu novamente.'''
      input('\nDigite uma tecla para voltar ao menu principal...')
      main()

def opcao_invalida():
      '''Função para lidar com opções inválidas. Exibe uma mensagem de erro informando que a opção escolhida é inválida e chama a função voltar_ao_menu_principal() para retornar ao menu principal.'''
      print('Opção inválida!\n')
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):
      '''Função para exibir um subtítulo. Limpa a tela e exibe o texto fornecido como um subtítulo, cercado por linhas de asteriscos para destacar a seção atual do programa.'''
      os.system('cls')
      linha = '*' * (len(texto) + 1)
      print(linha)
      print(texto)
      print(linha)
      print()

def escolher_novo_restaurante():
      '''Função para cadastrar um novo restaurante. Solicita o nome e a categoria do restaurante, e adiciona um novo dicionário à lista de restaurantes. O restaurante é adicionado como desativado por padrão.
      
      Inputs: - Nome do Restaurante
            - Categoria do Restaurante
      Outputs: - Adiciona um novo restaurante'''
      
      exibir_subtitulo('Cadastro de novo restaurante')
      nome_do_restaurante = input(f'Digite o nome do restaurante que deseja cadastrar: ')
      categoria = input(f'Digite a categoria do restaurante: {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
      voltar_ao_menu_principal()

def listar_restaurantes():
      '''Função para listar os restaurantes cadastrados. Exibe uma tabela com o nome, categoria e status (ativado/desativado) de cada restaurante na lista de restaurantes.'''
      exibir_subtitulo('Lista de restaurantes cadastrados')
      
      print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
      voltar_ao_menu_principal()

def alternar_estado_restaurante():
      '''Função para ativar ou desativar um restaurante. Solicita ao usuário o nome do restaurante que deseja ativar ou desativar, e alterna o status do restaurante correspondente na lista de restaurantes. Se o restaurante for encontrado, exibe uma mensagem indicando se ele foi ativado ou desativado. Se o restaurante não for encontrado, exibe uma mensagem de erro.'''
      exibir_subtitulo('Alternando o estado do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
      restaurante_encontrado = False
      for restaurante in restaurantes:
            if restaurante['nome'] == nome_restaurante:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
                  print(mensagem)
      if not restaurante_encontrado:
            print(f'Não foi encontrado um restaurante com o nome {nome_restaurante}.\n')
      
      voltar_ao_menu_principal()


def escolher_opcao():
      '''Função para escolher uma opção do menu. Solicita ao usuário que escolha uma opção e executa a função correspondente com base na escolha. Se a opção escolhida for inválida, chama a função opcao_invalida() para lidar com o erro.'''
      try:
      opcao_escolhida = int(input('Escolha uma opção: '))

      if opcao_escolhida == 1:
            escolher_novo_restaurante()
      elif opcao_escolhida == 2:
            listar_restaurantes()
      elif opcao_escolhida == 3:
            alternar_estado_restaurante()
      elif opcao_escolhida == 4:  # <-- Agora o 4 tem o seu lugar exclusivo!
            finalizar_app()
      else:                       # <-- O else agora só pega números errados
            opcao_invalida()
      except:
      opcao_invalida()

def main():
      '''Função principal do programa. Limpa a tela, exibe o nome do programa, as opções do menu e chama a função escolher_opcao() para iniciar a interação com o usuário.'''
      os.system('cls')
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()

if __name__ == '__main__':
      '''Ponto de entrada do programa. Verifica se o script está sendo executado diretamente e, em caso afirmativo, chama a função main() para iniciar o programa.'''
      main()