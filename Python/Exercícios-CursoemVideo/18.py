#Exercício 18
"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

import math

angulo= float(input("digite um angulo: "))

angulor = math.radians(angulo)

print(f"o seno de {angulo} é: {math.sin(angulor):.2f}")
print(f"o cosseno de {angulo} é: {math.cos(angulor):.2f}")
print((f"a tangente de {angulo} é {math.tan(angulor):.2f}"))
