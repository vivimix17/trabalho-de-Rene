from art import text2art

banner_text = text2art("Notícias - PB")
print(banner_text)

noticias = []
admins = {}
users = {}
users_info = {}
usuario_logado = None

def cadastrar_admin():
    username = input("Digite o nome de usuário do administrador: ")
    if username in admins:
        print("Nome de usuário já existe. Escolha outro.")
        return
    password = input("Digite a senha do administrador: ")
    verification_info = input("Digite sua informação pessoal adicional: ")
    admins[username] = password
    users_info[username] = verification_info
    print("Administrador cadastrado com sucesso.")



def login():
    global usuario_logado
    username = input("Nome de usuário: ")
    password = input("Senha: ")

    if username in admins and admins[username] == password:
        verification_info = input("Digite sua informação pessoal adicional: ")
        if verification_info == users_info.get(username, None):
            print("Login bem-sucedido como administrador.")
            usuario_logado = username
        else:
            print("Informação pessoal incorreta. Tente novamente.")
    elif username in users and users[username] == password:
        verification_info = input("Digite sua informação pessoal adicional: ")
        if verification_info == users_info[username]:
            print("Login bem-sucedido como usuário.")
            usuario_logado = username
        else:
            print("Informação pessoal incorreta. Tente novamente.")
    else:
        print("Nome de usuário ou senha incorretos. Tente novamente.")


def cadastrar_usuario():
    username = input("Digite o nome de usuário do usuário: ")
    if username in users or username in admins:
        print("Nome de usuário já existe. Escolha outro.")
        return
    password = input("Digite a senha do usuário: ")
    users[username] = password
    users_info[username] = input("Digite sua informação pessoal adicional: ")
    print("Usuário cadastrado com sucesso.")

def menu_admin():
    global usuario_logado
    while usuario_logado:
        print("\nMenu do Administrador")
        print("1. Inserir Notícia")
        print("2. Listar Notícias")
        print("3. Excluir Notícia")
        print("4. Editar Notícia")
        print("5. Buscar Notícia")
        print("6. Ordenar por ordem decrecente Notícia")
        print("7. Logout")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            inserir_noticia()
        elif choice == '2':
            listar_noticias()
        elif choice == '3':
            excluir_noticia()
        elif choice == '4':
            editar_noticia()
        elif choice == '5':
            buscar_noticia()
        elif choice == '7':
            usuario_logado = None
        elif choice == '6':
            exibir_noticias_adm()

def exibir_noticias_adm():
    print("\nNotícias do Editor (Ordem Decrescente por Curtidas):")
    noticias_editor = [noticia for noticia in noticias if noticia['editor'] == usuario_logado]
    noticias_editor.sort(key=lambda x: x['curtidas'], reverse=True)
    for i, noticia in enumerate(noticias_editor):
        print(f"{i + 1}. Título: {noticia['titulo']}")
        print(f"   Autor: {noticia['autor']}")
        print(f"   Curtidas: {noticia['curtidas']}")
        print("   Comentários:")
        for comentario in noticia['comentarios']:
            print(f"       {comentario}")
    if not noticias_editor:
        print("Nenhuma notícia disponível.")

def inserir_noticia():
    titulo = input("Título da notícia: ")
    conteudo = input("Conteúdo da notícia: ")
    noticias.append({"titulo": titulo, "conteúdo": conteudo, "autor": usuario_logado, "comentarios": [], "curtidas": 0})
    print("Notícia inserida com sucesso.")

def listar_noticias():
    print("\nLista de Notícias:")
    for i, noticia in enumerate(noticias):
        print(f"{i + 1}. Título: {noticia['titulo']}")
        print(f"   Autor: {noticia['autor']}")
        print(f"   Curtidas: {noticia['curtidas']}")
        print("   Comentários:")
        for comentario in noticia['comentarios']:
            print(f"       {comentario}")
    if not noticias:
        print("Nenhuma notícia disponível.")

def excluir_noticia():
    titulo = input("Digite o título da notícia a ser excluída: ")
    for noticia in noticias:
        if noticia['titulo'] == titulo:
            noticias.remove(noticia)
            print(f"Notícia '{titulo}' excluída com sucesso.")
            break
    else:
        print(f"Notícia '{titulo}' não encontrada.")

def editar_noticia():
    titulo = input("Digite o título da notícia a ser editada: ")
    for noticia in noticias:
        if noticia['titulo'] == titulo and noticia['autor'] == usuario_logado:
            novo_conteudo = input("Novo conteúdo da notícia: ")
            noticia['conteúdo'] = novo_conteudo
            print("Notícia editada com sucesso.")
            break
    else:
        print(f"Notícia '{titulo}' não encontrada ou você não tem permissão para editá-la.")

def buscar_noticia():
    titulo = input("Digite o título da notícia que deseja buscar: ")
    for noticia in noticias:
        if noticia['titulo'] == titulo:
            print(f"Título: {noticia['titulo']}")
            print(f"Conteúdo: {noticia['conteúdo']}")
            print(f"Autor: {noticia['autor']}")
            break
    else:
        print(f"Notícia '{titulo}' não encontrada.")

def menu_usuario():
    global usuario_logado
    while usuario_logado in users:
        print("\nMenu do Usuário")
        print("1. Listar Notícias")
        print("2. Buscar Notícia")
        print("3. Comentar Notícia")
        print("4. Curtir Notícia")
        print("5. Logout")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            listar_noticias()
        elif choice == '2':
            buscar_noticia()
        elif choice == '3':
            comentar_noticia()
        elif choice == '4':
            curtir_noticia()
        elif choice == '5':
            usuario_logado = None

def comentar_noticia():
    titulo = input("Digite o título da notícia para comentar: ")
    for noticia in noticias:
        if noticia['titulo'] == titulo:
            comentario = input("Digite seu comentário: ")
            noticia['comentarios'].append(f"{usuario_logado}: {comentario}")
            print("Comentário adicionado com sucesso.")
            break
    else:
        print(f"Notícia '{titulo}' não encontrada.")

def curtir_noticia():
    titulo = input("Digite o título da notícia para curtir: ")
    for noticia in noticias:
        if noticia['titulo'] == titulo:
            noticia['curtidas'] += 1
            print(f"Você curtiu a notícia '{titulo}'.")
            break
    else:
        print(f"Notícia '{titulo}' não encontrada.")

while True:
    print("\nMenu Geral")
    print("1. Cadastrar Administrador")
    print("2. Login")
    print("3. Cadastrar Usuário")
    print("4. Cadastrar Notícia Anônima")
    print("0. Sair")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        cadastrar_admin()
    elif choice == '2':
        login()
    elif choice == '3':
        cadastrar_usuario()
    elif choice == '4':
        inserir_noticia()
    elif choice == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")

    if usuario_logado in admins:
        menu_admin()
    elif usuario_logado in users:
        menu_usuario()