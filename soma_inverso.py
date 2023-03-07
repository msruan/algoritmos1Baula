#33. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.

#entrada
numero = int(input('Digite um número: '))

#proces
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10
inverso = unidade * 100 + dezena * 10 + centena
soma = inverso + numero

#saída
print('A soma vale',soma)