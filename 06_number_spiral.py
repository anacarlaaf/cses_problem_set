# todos com índice 1 tão dando 0
# tirar index

t = int(input())
casos = []
for i in range(t):
    y, x = list(map(int, input().split()))
    casos.append([y, x])

# verificar qual o maior quadrado formado
maior = 0
for i in casos:
    if i[0] > maior:
        maior = i[0]
    if i[1] > maior:
        maior = i[1]
print(maior)

resultado = []
linha = 1
coluna = 1
lado = 1
numero = 1

coord_numero = {(1, 1): 1, }

while lado < maior:
    coluna += 1
    numero += 1
    # print(numero, [linha, coluna])
    coord_numero[(linha, coluna)] = numero
    while linha < lado + 1:
        linha += 1
        numero += 1
        # print(numero, [linha, coluna])
        coord_numero[(linha, coluna)] = numero
    while coluna > 1:
        coluna -= 1
        numero += 1
        # print(numero, [linha, coluna])
        coord_numero[(linha, coluna)] = numero
    lado += 1
    linha += 1
    numero += 1
    # print(numero, [linha, coluna])
    coord_numero[(linha, coluna)] = numero
    while coluna < lado + 1:
        coluna += 1
        numero += 1
        # print(numero, [linha, coluna])
        coord_numero[(linha, coluna)] = numero
    while linha > 1:
        linha -= 1
        numero += 1
        # print(numero, [linha, coluna])
        coord_numero[(linha, coluna)] = numero
    lado += 1

for i in casos:
    linha = i[0]
    coluna = i[1]
    # print(coord_numero[(linha, coluna)])
for i in coord_numero:
    print(i, " - ", coord_numero[i])
