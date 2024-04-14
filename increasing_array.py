size = int(input())
numbers = map(int, input().split())

movements = 0
anterior = 0
for i in numbers:
    if i < anterior:
        movements += anterior-i
        anterior = i+(anterior-i)
    else:
        anterior = i
print(movements)
