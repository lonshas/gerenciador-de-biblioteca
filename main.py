import csv
import os
os.system("cls")

estrutura_de_livro = ['titulo','autor','ano','codigo','status']

def cadastro_de_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicacao do livro: ")
    codigo = input("Digite o codigo(ISBN) do livro: ")
    status = "Disponivel"
    
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


def emprestimo_de_livro():
    if not os.path.exists('livros.csv'): 
        print("Nenhum livro cadastrado.") 
        return 
    codigo_busca = input("Digite o código (ISBN) do livro que deseja emprestar: ")
    livros = []
    livros_encontrados = []
    # Lê todos os livros do arquivo 
    with open('livros.csv', 'r', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        for livro in leitor:
            livros.append(livro)
        if livro['codigo'] == codigo_busca:
            livros_encontrados.append(livro)
    # Verifica se encontrou algum livro
    if len(livros_encontrados) == 0:
        print("Nenhum livro encontrado com esse código.")
        return
    # Mostra os livros encontrados
    print("\nLivros encontrados:")
    print("---------------------------------------------")
    for i, livro in enumerate(livros_encontrados, start=1):
        print(f"{i} - {livro['titulo']}")
        print(f" Autor: {livro['autor']}")
        print(f" Ano: {livro['ano']}")
        print(f" Status: {livro['status']}")
        print("---------------------------------------------")
    # Se houver apenas um livro
    if len(livros_encontrados) == 1:
        livro_escolhido = livros_encontrados[0]
    # Se houver vários livros
    else:
        escolha = input("Digite o número do livro que deseja emprestar: ")
        if not escolha.isdigit():
            print("Opção inválida.")
            return
        escolha = int(escolha)
        if escolha < 1 or escolha > len(livros_encontrados):
            print("Opção inválida.")
            return
        livro_escolhido = livros_encontrados[escolha - 1]
    # Verifica se o livro já está emprestado
    if livro_escolhido['status'] == 'Emprestado':
        print("Esse livro já está emprestado.")
        return
    # Altera o status do livro escolhido
    livro_escolhido['status'] = 'Emprestado'
    # Reescreve o arquivo CSV
    with open('livros.csv', 'w', newline='') as emprestimo:
        escritor = csv.DictWriter(emprestimo, fieldnames=estrutura_de_livro)
        escritor.writeheader()
        escritor.writerows(livros)
    print("\nLivro emprestado com sucesso!")

def listagem_de_livros():
    if not os.path.exists('livros.csv'):
        print("Nenhum livro cadastrado.")
        return
    livros = []
    with open('livros.csv', 'r', newline='') as listagem:
            leitor = csv.DictReader(listagem)
            for livro in leitor:
                livros.append(livro)

    ordem = input("Deseja ordenar a listagem por título, autor ou ano? (Digite 'titulo', 'autor' ou 'ano'): ")
    if ordem not in ['titulo', 'autor', 'ano']:
        print("Opção inválida. A listagem será feita na ordem de cadastro.")
        ordem = None
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
    with open('livros.csv', 'r', newline='') as listagem:
        leitor = csv.DictReader(listagem)
        for livro in leitor:
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano de publicacao: {livro['ano']}")
            print(f"Codigo: {livro['codigo']}")
            print(f"Status: {livro['status']}")
            print("-------------------------------------------------")


    

while True:
    print("----------Gerenciador da Biblioteca----------\n--------------------MENU---------------------\n")
    escolha_menu = input("1- CADASTRAR LIVRO\n2- EMPRÉSTIMO DE LIVRO\n3- DEVOLUÇÃO DE LIVRO\n4- LISTAR LIVROS\n5- BUSCAR LIVRO\n6- SAIR\nEscreva o comando aqui: ")
    if escolha_menu == "1":
        cadastro_de_livro()
    elif escolha_menu =="2":
        emprestimo_de_livro()
    elif escolha_menu =="3":
        pass
    elif escolha_menu =="4":
        listagem_de_livros()
    elif escolha_menu =="5":
        pass
    elif escolha_menu =="6":
        break
    else:
        print("Comando inválido!")