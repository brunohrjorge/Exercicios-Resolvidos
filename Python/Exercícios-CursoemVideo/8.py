#Exercício 8
"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

metros= float(input("Digite os metros: "))

cent= metros * 100
mili= metros * 1000

print(f"{metros} metros sao {cent} centimetros e {mili} milimetros")