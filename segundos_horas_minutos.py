#27. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

#entrada
seg = int(input('Quantos segundos? '))

#proces
hor = seg // 3600
min = seg // 60 - (hor * 60)
seconds = seg % 60

#saída
print("Isso corresponde a",hor,'horas,',min,'minutos e',seconds,'segundos')