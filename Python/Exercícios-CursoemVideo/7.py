#Exercício 7
"""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média"""

soma= 0

for i in range(2):
    nota= float(input("digite sua nota: "))
    soma += nota

media= soma/2

print(f"a sua media foi: {media}")