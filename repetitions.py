dna = input()
max_repeticoes = 1
repeticoes = 1
anterior = "O"
for i in dna:
    if i == anterior:
        repeticoes += 1
    else:
        repeticoes = 1
    anterior = i
    if repeticoes > max_repeticoes:
        max_repeticoes = repeticoes
print(max_repeticoes)
