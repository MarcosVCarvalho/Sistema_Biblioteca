import json
import os
import datetime

catalogo_livros = []
catalogo_usuarios = []
ids_existentes = []
registros_emprestimos = []
contador_id = 0
arquivo_json = 'catalogo.json'

def carregar_dados_json():
    global catalogo_livros, catalogo_usuarios, ids_existentes, registros_emprestimos, contador_id
    if os.path.exists(arquivo_json):
        try:
            with open(arquivo_json, 'r') as arquivo:
                dados = json.load(arquivo)
                catalogo_livros = dados.get('livros', [])
                catalogo_usuarios = dados.get('usuarios', [])
                registros_emprestimos = dados.get('emprestimos', [])
                ids_existentes = [livro['id'] for livro in catalogo_livros] + [usuario['id'] for usuario in catalogo_usuarios]
                contador_id = max(ids_existentes, default=0)
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON. O arquivo pode estar vazio ou corrompido.")
            # Inicializa os dados com listas vazias
            catalogo_livros.clear()
            catalogo_usuarios.clear()
            registros_emprestimos.clear()
            ids_existentes.clear()
            contador_id = 0
    else:
        # Se o arquivo não existir, inicializa os dados
        catalogo_livros.clear()
        catalogo_usuarios.clear()
        registros_emprestimos.clear()
        ids_existentes.clear()
        contador_id = 0

# Gera um id único
def gerar_id_unico(maximo=9999):
    global contador_id
    contador_id += 1
    if contador_id > maximo:
        contador_id = 1  # Reinicia o contador se atingir o máximo
    return contador_id

def salvar_dados_em_json():
    dados = {
        'livros': catalogo_livros,
        'usuarios': catalogo_usuarios,
        'emprestimos': registros_emprestimos
    }
    with open(arquivo_json, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def criar_titulo(tex):
    print('='*80)
    print(f'{tex}'.center(80))
    print('='*80)

def Adicionarnovolivro(titulo, autor, ano_publicacao):
    livro = {
        'id': gerar_id_unico(),
        'titulo': titulo,
        'autor': autor,
        'ano_publicacao': ano_publicacao,
        'disponivel': True
    }
    ids_existentes.append(livro['id'])
    catalogo_livros.append(livro)
    salvar_dados_em_json()
    return livro['id']

def Listartodososlivros():
    print(f"{'ID':<5} {'Título':<30} {'Autor':<20} {'Ano':<10} {'Disponível':<12}")
    print("=" * 80)
    for livro in catalogo_livros:
        disponivel = 'Sim' if livro['disponivel'] else 'Não' 
        print(f"{livro['id']:<5} {livro['titulo']:<30} {livro['autor']:<20} {livro['ano_publicacao']:<10} {disponivel:<12}")

def Buscarlivroportítulo(titulo_a_buscar):
    resultado = []
    for livro in catalogo_livros:
        if titulo_a_buscar in livro['titulo'].upper():
            resultado.append(livro)
    return resultado

def Adicionarnovousuário(nome_usuario, email_usuario):
    usuario = {
        'id': gerar_id_unico(),
        'nome': nome_usuario,
        'email': email_usuario
    }
    ids_existentes.append(usuario['id'])
    catalogo_usuarios.append(usuario)
    salvar_dados_em_json()
    return usuario['id']

def Listartodososusuários():
    print(f"{'ID':<5}{'Nome do Usuario':<36} {'Email do Usuario':<36} ")
    print("=" * 80)
    for usuario in catalogo_usuarios:
        print(f"{usuario['id']:<5} {usuario['nome']:<36} {usuario['email']:<36}")

def atualizar_disponibilidade_livro(id_livro, disponivel):
    for livro in catalogo_livros:
        if id_livro == livro['id']:
            livro['disponivel'] = disponivel
            salvar_dados_em_json()
            return
    print('Erro! Livro indisponível no momento'.center(80))

def Verificador_para_emprestimo(id_usuario, id_livro):
    usuario_existe = any(usuario['id'] == id_usuario for usuario in catalogo_usuarios)
    livro_existe = any(livro['id'] == id_livro for livro in catalogo_livros)
    return usuario_existe and livro_existe

def realizar_emprestimo(id_livro_desejado, id_usuario):
    hoje = str(datetime.datetime.now())
    emprestimo = {
        'id': gerar_id_unico(),
        'id_livro': id_livro_desejado,
        'id_usuario': id_usuario,
        'data_emprestimo': hoje,
        'data_devolucao': 'xx/xx/xx'
    }
    atualizar_disponibilidade_livro(id_livro_desejado, False)
    registros_emprestimos.append(emprestimo)
    salvar_dados_em_json()
    return emprestimo['id']

def devolver_livro(id_emprestimo):
    for emprestimo in registros_emprestimos:
        if id_emprestimo == emprestimo['id']:
            hoje = str(datetime.datetime.now())
            emprestimo['data_devolucao'] = hoje
            atualizar_disponibilidade_livro(emprestimo['id_livro'], True)
            salvar_dados_em_json()
            return True
    print('Erro! ID não encontrado'.center(80))
    return False

def listar_emprestimos_ativos():
    print(f"{'ID':<5}{'Nome do Usuario':<36}{'Titulo do Livro':<36}")
    print("=" * 80)
    ativos_encontrados = False
    for emprestimo in registros_emprestimos:
        if emprestimo['data_devolucao'] == 'xx/xx/xx':
            ativos_encontrados = True
            for usuario in catalogo_usuarios:
                if usuario['id'] == emprestimo['id_usuario']:
                    for livro in catalogo_livros:
                        if livro['id'] == emprestimo['id_livro']:
                            print(f"{emprestimo['id']:<5}{usuario['nome']:<36}{livro['titulo']:<36}")
                            break
    if not ativos_encontrados:
        print('Sem empréstimos ativos'.center(80))

def historico_emprestimos_usuario(id_usuario):
    try:
        for usuario in catalogo_usuarios:
            if id_usuario == usuario['id']:
                nome = usuario['nome']
                print(f"Emprestimos do {nome}".center(80))
                print("=" * 80)
                print(f"{'ID':<5} {'Titulo do Livro':<36} {'Estado do Emprestimo':<36}")
                print("=" * 80)
                
                for emprestimo in registros_emprestimos:
                    if id_usuario == emprestimo['id_usuario']:
                        for livro in catalogo_livros:
                            if livro['id'] == emprestimo['id_livro']:
                                titulo_livro = livro['titulo']
                                estado = 'Ativo' if emprestimo['data_devolucao'] == 'xx/xx/xx' else 'Devolvido'
                                print(f"{emprestimo['id']:<5} {titulo_livro:<36} {estado:<36}")
                return  # Sai da função após listar os empréstimos do usuário
        print('Usuário não encontrado.'.center(80))
    
    except Exception as e:
        print(f'Erro! {e}. Tente novamente.')

carregar_dados_json()
