#Exercício 19
"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
 Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

from random import choice

lista= []

for i in range(4):
    aluno= str(input("digite o nome do aluno: "))
    lista.append(aluno)


print(choice(lista))