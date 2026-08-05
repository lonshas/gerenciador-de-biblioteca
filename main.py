import csv
import os
os.system("cls")

estrutura_de_livro = ['titulo','autor','ano de publicacao','código','status']

while True:
    print("----------Gerenciador da Biblioteca----------\n--------------------MENU---------------------\n")
    escolha_menu = input("1- CADASTRAR LIVRO\n2- EMPRÉSTIMO DE LIVRO\n3- DEVOLUÇÃO DE LIVRO\n4- LISTAR LIVROS\n5- BUSCAR LIVRO\n6- ORDENAR LISTA\n7- SAIR\nEscreva o comando aqui: ")
    if escolha_menu == "1":
        cadastro_de_livro()
    elif escolha_menu =="2":
        pass
    elif escolha_menu =="3":
        pass
    elif escolha_menu =="4":
        pass
    elif escolha_menu =="5":
        pass
    elif escolha_menu =="6":
        pass
    elif escolha_menu =="7":   
        break



def cadastro_de_livro():
    with open('livros.csv','a',newline= '') as cadastro:
        livro = {'titulo':titulo,'autor':autor,'ano de publicacao':ano,'código':isbn,'status':status}
        writer = csv.DictWriter('livros.csv',fieldnames=estrutura_de_livro)
        writer.writerow(livro)