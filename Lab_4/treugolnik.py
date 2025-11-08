n = int(input('введите кол-во строк: '))
m = int(input('введите кол-во столбцов: '))

for i in range(1, n+1):
    for j in range(i):
        print('#', end='')
    print()    