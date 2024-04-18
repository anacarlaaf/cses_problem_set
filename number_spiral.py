# Problema: Number Spiral
# Link: https://cses.fi/problemset/task/1071/

# Minha Lógica:
# Existe uma progressão aritmética na diagonal principal
# a1 = 1
# r = 2
# Usando as coordenadas posso saber o lado do quadrado que número está formando na espiral
# e calcular o valor pertencente a diagonal desse quadrado.
# Sabendo esse valor e se o lado do quadrado é par ou ímpar, posso saber se devo seguir no sentido horário
# ou anti-horário conforme as coordenadas e assim saber se devo somar ou subtrair para achar o resultado.

t = int(input())
resultado = []
for i in range(t):
    y, x = list(map(int, input().split()))

    numero = 1
    # saber o lado do quadrado
    if y == x or x > y:
        n = x - 1
    else:
        n = y - 1

    # soma de progressão aritmética
    an = 2 + (n - 1) * 2
    sn = (2 + an) * n // 2  # divisão inteira para não der ruim com números grandes
    numero += sn

    if y == x:
        resultado.append(numero)

    else:
        if n % 2 == 0:
            if y < x:
                numero += n + 1 - y
                resultado.append(numero)
            else:
                numero -= n + 1 - x
                resultado.append(numero)
        else:
            if y < x:
                numero -= n + 1 - y
                resultado.append(numero)
            else:
                numero += n + 1 - x
                resultado.append(numero)

for i in resultado:
    print(i)
