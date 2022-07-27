#Programa que lê dois números inteiros e compara-os
n1 =int(input('Digite o primeiro número:'))
n2 =int(input('Digite o segundo número:'))
if n1 > n2:
    print('O primeiro valor é maior')
elif n1 < n2:
    print('O segundo valor é maior')
else:
    print('Os números são iguais')
