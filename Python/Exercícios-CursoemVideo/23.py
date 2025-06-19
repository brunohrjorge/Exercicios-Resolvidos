#Exercício 23
"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados."""

num= int(input("digite um numero entre 0 a 9999: "))

numstr= str(f"{num:0>4}")

print(f"milhar= {numstr[0]}")
print(f"centena= {numstr[1]}")
print(f"dezena= {numstr[2]}")
print(f"unidade= {numstr[3]}")




