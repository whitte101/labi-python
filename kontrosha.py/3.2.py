a = int(input('введите N: '))

for i in range(1, a + 1):
    for j in range(i):
        print(i, end = '')
    print()