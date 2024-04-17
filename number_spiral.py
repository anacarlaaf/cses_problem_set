# existe uma progressão aritmética na diagonal principal
    # a1 = 1
    # r = 2
# usando as coordenadas posso saber a qual quadrado pertence o número e calcular o valor pertencente a diagonal
# sabendo esse valor e se o lado é par ou ímpar, posso "subir" ou "descer" conforme a coordenada e somar ou
# subtrair para achar o resultado
# assim evito iterrar sobre cada coordenada

t = int(input())
resultado = []
numero = 1
lado = 0
for i in range(t):
    y, x = list(map(int, input().split()))
    if y == x:
        n = x-1
        an = 2 + (n-1)*2
        sn = (2 + an)*n/2
        numero += sn
        resultado.append(int(numero))
    elif y > x:
        n = y-1
    elif x > y:
        n = x-1
for i in resultado:
    print(i)
