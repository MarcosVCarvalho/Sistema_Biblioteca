import random
catalogo_livros = []
catalogo_usuarios = []
ids_existentes = []
registros_emprestimos = []
contador_id = 0

#Gera um id de 1 a 9999
def gerar_id_unico( maximo=9999,):
        global contador_id
        contador_id += 1
        novo_id = contador_id 
        if novo_id not in ids_existentes and novo_id <= maximo:
            return novo_id

#Mande uma str e a função. Retorna ela em titulo    
def criar_titulo(tex):
    print('='*80)
    print(f'{tex}'.center(80))
    print('='*80)

#Mande o titulo,autor e ano de publicação. irá ser adicionado a um livro
def Adicionarnovolivro(titulo, autor, ano_publicacao):
    livro = {}
    livro.clear()
    
    id = gerar_id_unico()
    ids_existentes.append(id)
    livro['id'] = id
    livro['titulo'] = titulo
    livro['autor'] = autor
    livro['ano_publicacao'] = ano_publicacao
    livro['disponivel'] = True
    catalogo_livros.append(livro.copy())
    return id

#Lista todos os livros em catalogo_livros
def Listartodososlivros():
    print(f"{'ID':<5} {'Título':<30} {'Autor':<20} {'Ano':<10} {'Disponível':<12}")
    print("=" * 80)
    for livro in catalogo_livros:
        disponivel = 'Sim' if livro['disponivel'] == True else 'Não' 
        print(f"{livro['id']:<5} {livro['titulo']:<30} {livro['autor']:<20} {livro['ano_publicacao']:<10} {disponivel:<12}")

#Mande um titulo. Retorna o resultado da busca
def Buscarlivroportítulo(titulo_a_buscar):
    resultado = []
    for livro in catalogo_livros:
        if titulo_a_buscar in livro['titulo'].upper() :
            resultado.append(livro)
    return resultado

#Mande o nome e email. Será adicionado a um usuario
def Adicionarnovousuário(nome_usuario, Email_usuario):
    usuario = {}
    usuario.clear()
    
    id = gerar_id_unico()
    ids_existentes.append(id)
    usuario['id'] = id
    usuario['nome'] = nome_usuario
    usuario['email'] = Email_usuario
    catalogo_usuarios.append(usuario.copy())

    return id

#Lista todos os usuarios em catalogo_usuarios
def Listartodososusuários():
    print(f"{'ID':<5}{'Nome do Usuario':<36} {'Email do Usuario':<36} ")
    print("=" * 80)
    for usuario in catalogo_usuarios:
        print(f"{usuario['id']:<5} {usuario['nome']:<36} {usuario['email']:<36}")

#Mande o id do livro e se ele deve estar disponivel ou não
def atualizar_disponibilidade_livro(id_livro, disponivel):
    for livro in catalogo_livros:
        if id_livro == livro['id']:
            livro['disponivel'] = disponivel
            return
    print('Erro! Livro indisponível no momento'.center(80))

#Mande o id de usuario e de livro. Verificará se eles existem no sistema
def Verificador_para_emprestimo(id_usuario, id_livro):

    usuario_existe = any(usuario['id'] == id_usuario for usuario in catalogo_usuarios)
    livro_existe = any(livro['id'] == id_livro for livro in catalogo_livros)
    if usuario_existe and livro_existe == True:
        return True
    
#Mande o id do livro, usuario. Irá realizar o emprestimo com a data de hoje
def realizar_emprestimo(id_livro_desejado, id_usuario, data_emprestimo):
    emprestimo = {}
    emprestimo.clear()

    id = gerar_id_unico()
    ids_existentes.append(id)
    emprestimo['id'] = id
    emprestimo['id_livro'] = id_livro_desejado
    emprestimo['id_usuario'] = id_usuario
    emprestimo['data_emprestimo'] = data_emprestimo
    emprestimo['data_devolucao'] = False
    atualizar_disponibilidade_livro(id_livro_desejado,False)
    registros_emprestimos.append(emprestimo.copy())
    return id

#Mande o id do emprestimo e a data da devolução. Irá atualizar no sistema
def devolver_livro(id_emprestimo, data_devolucao):
    for emprestimo in registros_emprestimos:
        if id_emprestimo == emprestimo['id']:
            emprestimo['data_devolucao'] = data_devolucao
            atualizar_disponibilidade_livro(emprestimo['id_livro'], True)
            return
    print('Erro! ID não encontrado'.center(80))

#Mostrar os emprestimos ativos
def listar_emprestimos_ativos():
        print(f"{'ID':<5}{'Nome do Usuario':<36}{'Titulo do Livro':<36} ")
        print("=" * 80)
        for emprestimo in registros_emprestimos:
            for usuario in catalogo_usuarios:
                for livro in catalogo_livros:
                    if usuario['id'] == emprestimo['id_usuario'] and emprestimo['data_devolucao'] == False and livro['id'] == emprestimo['id_livro']:
                        try:
                            print(f"{emprestimo['id']:<5}{usuario['nome']:<36}{livro['titulo']:<36}")
                        except:
                            print('Sem emprestimos ativos')

#Mande o id de usuario. Mostrará seu historico de emprestimos
def historico_emprestimos_usuario(id_usuario):
    try:
        for usuario in catalogo_usuarios:
            if id_usuario == usuario['id']:
                nome = usuario['nome']
        print(f"Emprestimos do {nome}".center(80))
        print("=" * 80)
        print(f"{'ID':<5} {'Titulo do Livro':<36} {'Estado do Emprestimo':<36} ")
        print("=" * 80)
        for emprestimo in registros_emprestimos:
            if id_usuario == emprestimo['id_usuario']:
                id_emprestimo = emprestimo['id']
                if emprestimo['data_devolucao'] == False:
                    estado_emprestimo = 'Ativo'
                else:
                    estado_emprestimo = 'Devolvido'
                for livro in catalogo_livros:
                    if livro['id'] == emprestimo['id_livro']:
                        titulo_livro = livro['titulo'] 
            print(f"{id_emprestimo:<5} {titulo_livro:<36} {estado_emprestimo:<36}")    
    except:
        print('Erro! Tente Novamente')