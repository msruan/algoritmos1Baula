#Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:

#entrada
a = int(input('Qual o primeiro número? '))
b = int(input('Qual o segundo? '))
c = int(input('Qual é o terceiro número? '))

#process
r = (a + b) ** 2
s = (b + c) ** 2
d = (r + s) / 2

#saída
print("O resultado é",d)