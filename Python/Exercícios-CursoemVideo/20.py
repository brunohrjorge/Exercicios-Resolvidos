#Exercício 20
"""O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import choice

lista= []

for i in range(4):
    aluno= str(input("digite o nome do aluno: "))
    lista.append(aluno)


for i in range(len(lista)):
    escolha= choice(lista)
    print(escolha)
    lista.remove(escolha)