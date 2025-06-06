import random
catalogo_livros = []
catalogo_usuarios = []
livro = ids_existentes = []
def OpcaoValida(a):
    try:
        if a in range(11):
            return a
        else:
            print('ERRO! Opção deve estar entre 0 e 10.'.center(80))

    except ValueError:
        print('ERRO! Digite uma opção validade'.center(80))
        return None
    
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

    return None

def Listartodososlivros():
    print(f"{'ID':<5} {'Título':<30} {'Autor':<20} {'Ano':<10} {'Disponível':<12}")
    print("=" * 80)
    for livro in catalogo_livros:
        id_livro = livro['id']
        titulo = livro['titulo']
        autor = livro['autor']
        ano_publicacao = livro['ano_publicacao']
        disponivel = "Sim" if livro['disponivel'] else "Não"
        
        print(f"{id_livro:<5} {titulo:<30} {autor:<20} {ano_publicacao:<10} {disponivel:<12}")

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

    return None

def Listartodososusuários():
    print(f"{'ID':<5}{'Nome do Usuario':<36} {'Email do Usuario':<36} ")
    print("=" * 80)
    for usuario in catalogo_usuarios:
        nome_usuario = usuario['nome']
        email = usuario['email']
        id_usuario = usuario['id']
        
        print(f"{id_usuario:<5} {nome_usuario:<36} {email:<36}")