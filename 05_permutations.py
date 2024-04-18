# Link do Problema: https://cses.fi/problemset/task/1070

n = int(input())
lista = [i for i in range(1, n+1)]

beautiful = 0
permutados = []
if n == 1:
    print(n)
elif len(lista) > 3:
    anterior = 0
    for i in lista:
        if i - anterior != 1 and anterior - i != 1:
            permutados.append(i)
            anterior = i
        else:
            lista.append(i)  # add para eles passarem de novo na verificacao
    print(*permutados)
else:
    print("NO SOLUTION")
