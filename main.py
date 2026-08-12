import csv
import os
os.system("cls")

print("Feito por: Estevão Guaitolini de Oliveira Rosa\n")

estrutura_de_livro = ['titulo','autor','ano','codigo','status']

"""Função para cadastrar um novo livro, pedindo ao usuário as informações necessárias como uma variável
e salvando em um arquivo CSV."""
def cadastro_de_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicacao do livro: ")
    codigo = input("Digite o codigo(ISBN) do livro: ")
    status = "Disponivel"

#Caso o arquivo já exista, ele apenas adiciona o novo livro ao final do arquivo.
#Caso não exista, ele cria o arquivo e adiciona o cabeçalho antes de adicionar o livro.
    arquivo_existe = os.path.exists('livros.csv')
    with open('livros.csv','a',newline= '') as cadastro:

        livro = {'titulo': titulo,
                'autor': autor,
                'ano': ano,
                'codigo': codigo,
                'status': status
                }
        
        writer = csv.DictWriter(cadastro,fieldnames=estrutura_de_livro)

        if not arquivo_existe:
            writer.writeheader()
        writer.writerow(livro)
    print("\nLivro cadastrado!")

"""Função para emprestar um livro, pedindo ao usuário o código do livro que deseja pegar emprestado por
meio da variável 'codigo_busca', verificando se o livro está disponível e atualizando o status
do livro "disponivel" para "emprestado" no arquivo CSV."""
def emprestimo_de_livro():
    if not os.path.exists('livros.csv'): 
        print("Nenhum livro cadastrado.") 
        return 
    codigo_busca = input("Digite o código (ISBN) do livro que deseja pegar emprestado: ")
    livros = []
    livros_encontrados = []

    with open('livros.csv', 'r', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for livro in leitor:
            livros.append(livro)
            if livro['codigo'] == codigo_busca:
                livros_encontrados.append(livro)
    
    if len(livros_encontrados) == 0:
        print("Nenhum livro disponivel encontrado com esse código.")
        return
    
    print("\nLivros encontrados:")
    print("---------------------------------------------")
    #lista todos os livros, com uma numeração para o usuário escolher qual deseja pegar emprestado.
    for i, livro in enumerate(livros_encontrados, start=1):
        print(f"{i} - Titulo: {livro['titulo']}")
        print(f" Autor: {livro['autor']}")
        print(f" Ano: {livro['ano']}")
        print(f" Status: {livro['status']}")
        print("---------------------------------------------")
    
    if len(livros_encontrados) == 1:
        livro_escolhido = livros_encontrados[0]
    
    else:
        escolha = input("Digite o número do livro que deseja pegar emprestado: ")
        if not escolha.isdigit():
            print("Opção inválida.")
            return
        escolha = int(escolha)
        if escolha < 1 or escolha > len(livros_encontrados):
            print("Opção inválida.")
            return
        livro_escolhido = livros_encontrados[escolha - 1]
    
    if livro_escolhido['status'] == 'Emprestado':
        print("Esse livro já está emprestado.")
        return
    
    livro_escolhido['status'] = 'Emprestado'
    
    with open('livros.csv', 'w', newline='') as emprestimo:
        escritor = csv.DictWriter(emprestimo, fieldnames=estrutura_de_livro)
        escritor.writeheader()
        escritor.writerows(livros)
    print("\nLivro emprestado com sucesso!")

# A devolução de livro funciona de forma idêntica ao empréstimo, mas ao invés de mudar o status
# para "emprestado", muda para "disponível".
def devolucao_de_livro():
    if not os.path.exists('livros.csv'): 
        print("Nenhum livro cadastrado.") 
        return 
    codigo_busca = input("Digite o código (ISBN) do livro que deseja devolver: ")
    livros = []
    livros_encontrados = []

    with open('livros.csv', 'r', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for livro in leitor:
            livros.append(livro)
            if livro['codigo'] == codigo_busca:
                livros_encontrados.append(livro)
    
    if len(livros_encontrados) == 0:
        print("Nenhum livro indisponivel encontrado com esse código.")
        return
    
    print("\nLivros encontrados:")
    print("---------------------------------------------")
    for i, livro in enumerate(livros_encontrados, start=1):
        print(f"{i} - {livro['titulo']}")
        print(f" Autor: {livro['autor']}")
        print(f" Ano: {livro['ano']}")
        print(f" Status: {livro['status']}")
        print("---------------------------------------------")
    
    if len(livros_encontrados) == 1:
        livro_escolhido = livros_encontrados[0]
    
    else:
        escolha = input("Digite o número do livro que deseja devolver: ")
        if not escolha.isdigit():
            print("Opção inválida.")
            return
        escolha = int(escolha)
        if escolha < 1 or escolha > len(livros_encontrados):
            print("Opção inválida.")
            return
        livro_escolhido = livros_encontrados[escolha - 1]
    
    if livro_escolhido['status'] == 'Disponivel':
        print("Esse livro já está disponível.")
        return
    
    livro_escolhido['status'] = 'Disponivel'
    
    with open('livros.csv', 'w', newline='') as emprestimo:
        escritor = csv.DictWriter(emprestimo, fieldnames=estrutura_de_livro)
        escritor.writeheader()
        escritor.writerows(livros)
    print("\nLivro devolvido com sucesso!")
    
# A listagem de livros escreve todos os livros cadastrados no arquivo CSV, podendo
# ordenar a listagem por título, autor ou ano.
def listagem_de_livros():
    if not os.path.exists('livros.csv'):
        print("Nenhum livro cadastrado.")
        return
    
    livros = []

    with open('livros.csv', 'r', newline='') as listagem:
            leitor = csv.DictReader(listagem)
            for livro in leitor:
                livros.append(livro)

#Caso a ordem de listagem seja inválida, a listagem será feita na ordem de cadastro.
    ordem = input("Deseja ordenar a listagem por título, autor ou ano? (Digite 'titulo', 'autor' ou 'ano'): ")
    if ordem not in ['titulo', 'autor', 'ano']:
        print("Opção inválida. A listagem será feita na ordem de cadastro.\n")
        ordem = None
#O sorted() ordena a lista de livros de acordo com a chave escolhida pelo usuário,
#utilizando uma função lambda para acessar o valor da chave no dicionário.
#A função lambda x: x representa uma função anônima.
#(nesse caso, representa cada livro na lista de livros, por isso é anônimo, pois representa vários livros ao mesmo tempo)
#que recebe um argumento x(titulo) e retorna o valor da chave especificada no dicionário x(lista 'livros').
    if ordem == 'titulo':
        with open('livros.csv', 'r', newline='') as listagem:
            leitor = csv.DictReader(listagem)
            livros = sorted(leitor, key=lambda x: x['titulo'])

    elif ordem == 'autor':
        with open('livros.csv', 'r', newline='') as listagem:
            leitor = csv.DictReader(listagem)
            livros = sorted(leitor, key=lambda x: x['autor'])

    elif ordem == 'ano':
        with open('livros.csv', 'r', newline='') as listagem:
            leitor = csv.DictReader(listagem)
            livros = sorted(leitor, key=lambda x: x['ano'])

    for livro in livros:
        print(f"Titulo: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de publicacao: {livro['ano']}")
        print(f"Codigo: {livro['codigo']}")
        print(f"Status: {livro['status']}")
        print("-------------------------------------------------")

# A busca de livros funciona de forma semelhante à listagem, mas ao invés de listar todos os livros,
# ela filtra os livros que contêm o termo de busca no título ou autor.
def buscar_livro():
    if not os.path.exists('livros.csv'):
        print("Nenhum livro cadastrado.")
        return
    
    termo_busca = input("Digite o título ou autor do livro que deseja buscar: ")
    livros_encontrados = []

#Esse .lower() serve para que a busca seja case insensitive, ou seja, não importa se o usuário
# digitar maiúsculas ou minúsculas, o programa vai encontrar o livro mesmo assim.
    with open('livros.csv', 'r', newline='') as busca:
        leitor = csv.DictReader(busca)
        for livro in leitor:
            if termo_busca.lower() in livro['titulo'].lower() or termo_busca.lower() in livro['autor'].lower():
                livros_encontrados.append(livro)
    
    if len(livros_encontrados) == 0:
        print("Nenhum livro encontrado com esse título ou autor.")
        return
    
    print("\nLivros encontrados:")
    print("---------------------------------------------")
    for i, livro in enumerate(livros_encontrados, start=1):
        print(f"{i} - {livro['titulo']}")
        print(f" Autor: {livro['autor']}")
        print(f" Ano: {livro['ano']}")
        print(f" Status: {livro['status']}")
        print("---------------------------------------------")

#Menu principal do programa, que chama as funções de acordo com a escolha do usuário.
while True:
    print("----------Gerenciador da Biblioteca----------\n--------------------MENU---------------------\n")
    escolha_menu = input("1- CADASTRAR LIVRO\n2- EMPRÉSTIMO DE LIVRO\n3- DEVOLUÇÃO DE LIVRO\n4- LISTAR LIVROS\n5- BUSCAR LIVRO\n6- SAIR\nEscreva o comando aqui: ")
    if escolha_menu == "1":
        cadastro_de_livro()
    elif escolha_menu =="2":
        emprestimo_de_livro()
    elif escolha_menu =="3":
        devolucao_de_livro()
    elif escolha_menu =="4":
        listagem_de_livros()
    elif escolha_menu =="5":
        buscar_livro()
    elif escolha_menu =="6":
        break
    else:
        print("Comando inválido!")