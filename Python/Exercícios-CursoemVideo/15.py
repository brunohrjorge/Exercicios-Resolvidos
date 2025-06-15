#Exercício 15
"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
 pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 15 centavos por km rodados."""

km= int(input("quantos km rodou?: "))
dias= int(input("por quantos dias?: "))
preco= (km*0.15) + (dias*60)

print(f"o preço é: {preco}")
