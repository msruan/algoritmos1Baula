#30. Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.

#entrada
min = int(input('Digite o número de minutos: '))

#proces
dias = min // 1440
horas = (min % 1440) // 60
minutos = (min % 1440) % 60

#saída
print('Isso corresponde a',dias,'dias,',horas,'horas e',minutos,'minutos!')