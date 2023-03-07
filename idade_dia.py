#36. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

#entrada
anos = int(input('Quantos anos? '))
mes = int(input('Quantos meses? '))
dias = int(input('Quantos dias? '))

#process
idade = anos * 365 + mes * 30 + dias 

#saída
print("A idade é de",idade,'dias!')