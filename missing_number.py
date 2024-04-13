n = int(input())
# usar o set() quando a ordem não importa torna a execucao mais rapida
incompleta = set(map(int, input().split()))

for i in range(1, n+1):
    if i not in incompleta:
        faltando = i
        break
print(faltando)
