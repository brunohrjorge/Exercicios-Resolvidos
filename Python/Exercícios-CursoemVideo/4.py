#Exercício 4
"""Faça um programa que leia algo pelo teclado e diga seu tipo
primitivo e todas as informações possíveis sobre ela"""

num= str(input("Digite algo: "))

print(f"{num} é alfanumérico? {num.isalnum()}")
print(f"{num} é alfabético? {num.isalpha()}")
print(f"{num} esta tudo em minúsculas? {num.islower()}")
print(f"{num} esta tudo em maiúsculas ? {num.isupper()}")
print(f"{num} todos são dígitos numéricos ? {num.isdigit()}")

