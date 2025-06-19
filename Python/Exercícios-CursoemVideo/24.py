#Exercício 24
"""Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"."""

cidade= str(input("digite o nome da cidade: ")).strip().lower()

primeironome= cidade.split()[0]

if primeironome == "santo":
    print("essa cidade começa com santo")
else:
    print("nao, essa cidade nao começa com santo")





