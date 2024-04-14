t = int(input())
casos = []
for i in range(t):
    y, x = list(map(int, input().split()))
    casos.append([y, x])
print(casos)

# encontrar maior linha e maior coluna
m_linha = 0
m_coluna = 0
for c in casos:
    if c[0] > m_linha:
        m_linha = c[0]
    if c[1] > m_coluna:
        m_coluna = c[1]
maximo = [m_linha, m_coluna]
print(maximo)

# gerar todos os números até maior linha e a maior coluna
