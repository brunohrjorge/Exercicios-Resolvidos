#Exercício 11

"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
 de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

larg= float(input("digite a largura: "))
alt= float(input("digite a altura: "))
area= larg * alt
tinta= area/2

print(f"sua parede tem uma area de {area} M2 e será necessário {tinta} litros de tinta")