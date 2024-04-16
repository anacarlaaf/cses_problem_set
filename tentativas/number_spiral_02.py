t = int(input())
casos = []
for i in range(t):
    y, x = list(map(int, input().split()))
    casos.append([y, x])
# print(casos)

resultado = []

# verificar qual o maior quadrado formado
maior = 0
for i in casos:
    if i[0] > maior:
        maior = i[0]
    elif i[1] > maior:
        maior = i[1]

# formar todos os valores até o maior quadrado
linha = 1
coluna = 1
lado = 1
numero = 1
while lado <= maior:
    # verificar se o quadrado formado tem valor par ou impar
    # para definir se a espiral continua em sentido horário
    # ou anti-horário
    if lado % 2 != 0:  # ímpar
        coluna += 1
        numero += 1
        print(numero, [linha, coluna])
        if [linha, coluna] in casos:
            resultado.append(numero)
        while linha < lado + 1:
            linha += 1
            numero += 1
            print(numero, [linha, coluna])
            if [linha, coluna] in casos:
                resultado.append(numero)
        while coluna > 1:
            coluna -= 1
            numero += 1
            print(numero, [linha, coluna])
            if [linha, coluna] in casos:
                resultado.append(numero)
        lado += 1
    else:
        linha += 1
        numero += 1
        print(numero, [linha, coluna])
        if [linha, coluna] in casos:
            resultado.append(numero)
        while coluna < lado + 1:
            coluna += 1
            numero += 1
            print(numero, [linha, coluna])
            if [linha, coluna] in casos:
                resultado.append(numero)
        while linha > 1:
            linha -= 1
            numero += 1
            print(numero, [linha, coluna])
            if [linha, coluna] in casos:
                resultado.append(numero)
        lado += 1
print(resultado)
