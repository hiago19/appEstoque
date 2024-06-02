from time import sleep

LINE = '-' * 50
DELAY_TIMES = [1, 2]
MAX_ATTEMPTS = 3


def mostrar_linhas():
    print(LINE)


def delay():
    for i in DELAY_TIMES:
        print("Carregando...")
        sleep(i)


def cadastro():
    while True:
        nome = input("Por favor, insira seu nome: ")
        idade = input("Agora, digite sua idade: ")

        if not idade.isdigit():
            print("Idade inválida! Por favor, insira um número.")
            continue

        username = input("Por favor, insira seu nome de usuário: ")
        delay()
        print(f'Seu nome de usuário foi criado, e é {username}.')

        password = input("Agora, por favor crie uma senha: ")
        password1 = input('Confirme sua senha: ')

        if password == password1:
            with open('usuarios.txt', 'a') as file:
                file.write(f"Usuário: {username} | Senha: {password}\n")
            break
        else:
            print('As senhas não são iguais!')

    delay()
    ldc = input('Usuário cadastrado com sucesso! \nDeseja fazer o login agora? sim ou não: ').lower()
    if ldc in ['sim', 's']:
        login()
    else:
        print(f'Obrigado pelo acesso, {nome}! \nVolte sempre!')


def login():
    tentativas = 0
    while tentativas < MAX_ATTEMPTS:
        username = input("Entre com seu nome de usuário: ")
        password = input("Coloque sua senha: ")

        with open('usuarios.txt', 'r') as loginfile:
            if f"Usuário: {username} | Senha: {password}\n" in loginfile.readlines():
                delay()
                print("\n Bem vindo!\n")
                menu()
            else:
                tentativas += 1
                print(f"\nCredenciais erradas! Tentativas restantes: {MAX_ATTEMPTS - tentativas}")
    print("Número máximo de tentativas excedido. Saindo...")
    delay()
    exit()


def ver_produtos():
    with open('estoque.txt', 'r') as arquivo:
        for linha in arquivo:
            posicoes = linha.split()
            if len(posicoes) >= 8:
                print(f"{posicoes[7]} peças {posicoes[1]} do {posicoes[4]} em estoque.")


def listar_produtos():
    with open('estoque.txt', 'r') as arquivo:
        for linha in arquivo:
            posicoes = linha.split()
            if len(posicoes) >= 5:
                print(posicoes[4])


def editar_produtos():
    with open('estoque.txt', 'r') as arquivo:
        conteudo = arquivo.read()

    antigo = input('Nome do produto a ser editado: ')
    novo = input('Nome do novo produto: ')
    string_nova = conteudo.replace(antigo, novo)

    with open('estoque.txt', 'w') as arquivo:
        arquivo.write(string_nova)

    delay()
    print('Produto Editado com sucesso!')


def adicionar_produto():
    tipo = input('Informe de que time é o produto que deseja adicionar: ')
    tamanho = input('Se é masculina ou feminina: ')
    quantidade = input('E quantos produtos você deseja adicionar: ')

    if not quantidade.isdigit():
        print("Quantidade inválida! Por favor, insira um número.")
        return

    delay()
    print('\nProduto adicionado, e cadastrado com sucesso!')

    with open('estoque.txt', 'a') as arquivo:
        arquivo.write(f"Gênero: {tamanho} | Time: {tipo} | Quantidade: {quantidade}\n")


def excluir_produtos():
    with open('estoque.txt', 'r') as arquivo:
        conteudo = arquivo.read()

    antigo = input('Nome do produto a ser excluido: ')
    string_nova = conteudo.replace(antigo, '')

    with open('estoque.txt', 'w') as arquivo:
        arquivo.write(string_nova)

    delay()
    print('Produto excluido com sucesso!')


def menu():
    while True:
        mostrar_linhas()
        print(' Menu')
        print('''
        [1] - Ver produtos.
        [2] - Adicionar produtos.
        [3] - Listar produtos.
        [4] - Deletar produtos.
        [5] - Editar produtos.
        [6] - Sair.
        ''')
        mostrar_linhas()
        escolha = int(input('Digite uma opção: '))

        if escolha == 1:
            ver_produtos()
        elif escolha == 2:
            adicionar_produto()
        elif escolha == 3:
            listar_produtos()
        elif escolha == 4:
            excluir_produtos()
        elif escolha == 5:
            editar_produtos()
        elif escolha == 6:
            print('Obrigado!\nVolte sempre.')
            break
        else:
            print('Opção inválida! Por favor, insira um número de 1 a 6.')


# PAGINA INICIAL
mostrar_linhas()
print('PAGINA INICIAL'.center(50))
mostrar_linhas()

inicio = input('Você é um usuário cadastrado? sim ou não: ').lower()

if inicio in ['sim', 's']:
    login()
elif inicio in ['nao', 'n', 'não']:
    cadastro()
else:
    print('Erro! Opção inválida.')
