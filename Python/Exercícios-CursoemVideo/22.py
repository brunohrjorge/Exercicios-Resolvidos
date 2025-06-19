#Exercício 22
"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao no total sem os espaços.
- Quantas letras tem o primeiro nome."""

nome= str(input("digite seu nome completo: ")).strip()


print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(" "))
posiçao= nome.index(" ")
print(len(nome[0:posiçao]))