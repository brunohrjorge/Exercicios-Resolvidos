#Exercício 17
"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
 de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa."""

catop= float(input("digite o cateto oposto: "))
catad= float(input("digite o cateto adjacente: "))
hipotenusa= (catop**2 + catad**2)**0.5

print(hipotenusa)