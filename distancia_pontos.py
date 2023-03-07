#Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles

#entrada
x1 = float(input('Qual a coordenada x do primeiro ponto? '))
y1 = float(input("Qual a coordenada y do primeiro ponto? "))
x2 = float(input('Qual a coordenada x do primeiro ponto'))
y2 = float(input('Digite o segundo número: '))

#process
resul = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

#saída
print('A distância entre os pontos é:',resul)