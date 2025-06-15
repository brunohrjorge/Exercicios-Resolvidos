#Exercício 9
"""Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada."""

num= int(input("didite um numero inteiro: "))

for i in range(1,11):
    print(f"{num} x {i:>2} = {num*i}")