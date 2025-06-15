#Exercício 12
"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""


produto= float(input("digite o preço do produto: "))

desconto= (5/100) * produto

print(f"o valor do produto com um desconto de 5% será: {produto-desconto}")