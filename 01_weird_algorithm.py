# Link do problema: https://cses.fi/problemset/task/1068

n = int(input())

outputs = []
while n != 1:
    outputs.append(int(n))
    if n % 2 == 0:
        n = n/2
    else:
        n = n*3+1
outputs.append(1)
print(*outputs)
