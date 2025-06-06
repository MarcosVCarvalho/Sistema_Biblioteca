import Funções
import time
import datetime

while True:
    print('='*80)
    print('Menu Principal'.center(80))
    print('='*80)
    print('1:Adicionar novo livro')
    print('2:Listar todos os livros')
    print('3:Buscar livro por título')
    print('4:Adicionar novo usuário')
    print('5:Listar todos os usuários')
    print('6:Realizar um empréstimo')
    print('7:Devolver um livro')
    print('8:Listar empréstimos ativos')
    print('9:Visualizar histórico de empréstimos de um usuário')
    print('10:Sair do sistema')
    print('='*80)

    try:
        op = int(input('Digite sua opção: '))
        if op in range(11):
            opcao_Valida = op
        else:
            print('ERRO! Opção deve estar entre 0 e 10.'.center(80))
            opcao_Valida = None

    except ValueError:
        print('ERRO! Digite uma opção validade'.center(80))
        opcao_Valida = None
    
    if opcao_Valida is not None:
        if opcao_Valida == 1:
            Funções.criar_titulo('Adicionar novo livro')
            titulo = input('titulo do livro: ')
            autor = input('Autor do livro: ')
            ano_publicacao = int(input('Ano de publicação: '))
            id_livro = Funções.Adicionarnovolivro(titulo, autor, ano_publicacao)
            print(f'Livro adicionado com sucesso - ID:{id_livro}'.center(80))

        elif opcao_Valida == 2:
            Funções.criar_titulo('Listar todos os livros')
            Funções.Listartodososlivros()
            
        elif opcao_Valida == 3:
            Funções.criar_titulo('Buscar livro por título')
            titulo_a_buscar = str(input('Qual o título do livro: ')).upper()
            livro_buscado = Funções.Buscarlivroportítulo(titulo_a_buscar)
            if livro_buscado:
                print(f'livros encontrados: {len(livro_buscado)}'.center(80))
                print("=" * 80)
                print(f"{'ID':<5} {'Título':<30} {'Autor':<20} {'Ano':<10} {'Disponível':<12}")
                print("=" * 80)
                for livro in livro_buscado:
                    print(f"{livro['id']:<5} {livro['titulo']:<30} {livro['autor']:<20} {livro['ano_publicacao']:<10} {livro['disponivel']:<12}")
            else:
                Funções.criar_titulo('Livro não encontrado')

        elif opcao_Valida == 4:
            Funções.criar_titulo('Adicionar novo usuário')
            nome_usuario = input('Nome do Usuario: ')
            email_usuario = input('Email do Usuario: ')
            id_usu = Funções.Adicionarnovousuário(nome_usuario, email_usuario)
            print(f'Usuario adicionado com sucesso - ID:{id_usu}'.center(80))

        elif opcao_Valida == 5:
            Funções.criar_titulo('Listar todos os usuários')
            Funções.Listartodososusuários()
        
        elif opcao_Valida == 6:
            Funções.criar_titulo('Realizar um empréstimo')
            id_usuario = int(input('Digite o id do usuario: '))
            id_livro_desejado = int(input('Digite o id do livro desejado: '))
            verificador = Funções.Verificador_para_emprestimo(id_usuario,id_livro_desejado)
            if verificador == True:
                data_emprestimo = datetime.datetime.now()
                id_emprestimo = Funções.realizar_emprestimo(id_livro_desejado, id_usuario, data_emprestimo)
                print(f'Emprestimo realizado com sucesso - ID:{id_emprestimo}')
            else:
                print('Erro! id de usuario ou livro inexistente'.center(80))

        elif opcao_Valida == 7:
            Funções.criar_titulo('Devolver um livro')
            id_emprestimo = int(input('Digite o id do emprestimo: '))
            data_devolucao = datetime.datetime.now()
            Funções.devolver_livro(id_emprestimo, data_devolucao)
            Funções.criar_titulo('Devolução realizada com sucesso')

        elif opcao_Valida == 8:
            Funções.criar_titulo('Listar empréstimos ativos')
            Funções.listar_emprestimos_ativos()
          
        elif opcao_Valida == 9:
            Funções.criar_titulo('Visualizar histórico de empréstimos de um usuário')
            id_usuario = int(input('Digite o id do usuario: '))
            Funções.historico_emprestimos_usuario(id_usuario)
           
        elif opcao_Valida == 10:
            Funções.criar_titulo('Fechando Menu - Volte Sempre')
            break
            