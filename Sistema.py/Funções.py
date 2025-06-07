import random
catalogo_livros = []
catalogo_usuarios = []
ids_existentes = []
registros_emprestimos = []

def gerar_id_unico(minimo=0, maximo=9999, max_tentativas=10000):
    global catalogo_livros
    global catalogo_usuarios
    global ids_existentes
    for _ in range(max_tentativas):
        novo_id = random.randint(minimo, maximo)
        if novo_id not in ids_existentes:
            return novo_id
        
def criar_titulo(tex):
    print('='*80)
    print(f'{tex}'.center(80))
    print('='*80)

def Adicionarnovolivro(titulo, autor, ano_publicacao):
    global catalogo_livros
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

def Listartodososlivros():
    global catalogo_livros
    print(f"{'ID':<5} {'Título':<30} {'Autor':<20} {'Ano':<10} {'Disponível':<12}")
    print("=" * 80)
    for livro in catalogo_livros:
        disponivel = 'Sim' if livro['disponivel'] == True else 'Não' 
        print(f"{livro['id']:<5} {livro['titulo']:<30} {livro['autor']:<20} {livro['ano_publicacao']:<10} {disponivel:<12}")

def Buscarlivroportítulo(titulo_a_buscar):
    global catalogo_livros
    resultado = []
    for livro in catalogo_livros:
        if titulo_a_buscar in livro['titulo'].upper() :
            resultado.append(livro)
    return resultado

def Adicionarnovousuário(nome_usuario, Email_usuario):
    global catalogo_usuarios
    usuario = {}
    usuario.clear()
    
    id = gerar_id_unico()
    ids_existentes.append(id)
    usuario['id'] = id
    usuario['nome'] = nome_usuario
    usuario['email'] = Email_usuario
    catalogo_usuarios.append(usuario.copy())

    return id

def Listartodososusuários():
    global catalogo_usuarios
    print(f"{'ID':<5}{'Nome do Usuario':<36} {'Email do Usuario':<36} ")
    print("=" * 80)
    for usuario in catalogo_usuarios:
        print(f"{usuario['id']:<5} {usuario['nome']:<36} {usuario['email']:<36}")

def atualizar_disponibilidade_livro(id_livro, disponivel):
    global catalogo_livros
    for livro in catalogo_livros:
        if id_livro == livro['id']:
            livro['disponivel'] = disponivel
            return
    print('Erro! Livro indisponível no momento'.center(80))

def Verificador_para_emprestimo(id_usuario, id_livro):
    global catalogo_livros
    global catalogo_usuarios

    usuario_existe = any(usuario['id'] == id_usuario for usuario in catalogo_usuarios)
    livro_existe = any(livro['id'] == id_livro for livro in catalogo_livros)
    if usuario_existe and livro_existe == True:
        return True
    
def realizar_emprestimo(id_livro_desejado, id_usuario, data_emprestimo):
    global registros_emprestimos
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

def devolver_livro(id_emprestimo, data_devolucao):
    global registros_emprestimos
    for emprestimo in registros_emprestimos:
        if id_emprestimo == emprestimo['id']:
            emprestimo['data_devolucao'] = data_devolucao
            atualizar_disponibilidade_livro(emprestimo['id_livro'], True)
            return
    print('Erro! ID não encontrado'.center(80))

def listar_emprestimos_ativos():
    global registros_emprestimos
    global catalogo_livros
    global catalogo_usuarios
    print(f"{'ID':<5}{'Nome do Usuario':<36}{'Titulo do Livro':<36} ")
    print("=" * 80)
    for emprestimo in registros_emprestimos:
        for usuario in catalogo_usuarios:
            for livro in catalogo_livros:
                if usuario['id'] == emprestimo['id_usuario'] and emprestimo['data_devolucao'] == False and livro['id'] == emprestimo['id_livro']:
                    nome_usuario = usuario['nome']
                    id_emprestimo = emprestimo['id']
                    titulo_livro = livro['titulo'] 
                    try:
                        print(f"{id_emprestimo:<5}{nome_usuario:<36}{titulo_livro:<36}")
                    except:
                        print('Sem emprestimos ativos')

def historico_emprestimos_usuario(id_usuario):
    global registros_emprestimos
    global catalogo_livros
    global catalogo_usuarios
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
        