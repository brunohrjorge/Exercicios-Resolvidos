#Exercício 25
"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome."""

nome= str(input("digite seu nome: ")).strip().lower()

nomediv= nome.split()

tem= 0


for i in nomediv:
    if "silva" in i:
        tem += 1

if tem > 0:
    print("esse nome tem silva")
else:
    print("esse nome nao tem silva")