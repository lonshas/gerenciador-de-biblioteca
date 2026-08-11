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

def listagem_de_livros():
    if not os.path.exists('livros.csv'):
        print("Nenhum livro cadastrado.")
        return
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
    escolha_menu = input("1- CADASTRAR LIVRO\n2- EMPRÉSTIMO DE LIVRO\n3- DEVOLUÇÃO DE LIVRO\n4- LISTAR LIVROS\n5- BUSCAR LIVRO\n6- ORDENAR LISTA\n7- SAIR\nEscreva o comando aqui: ")
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
        pass
    elif escolha_menu =="7":   
        break
    else:
        print("Comando inválido!")