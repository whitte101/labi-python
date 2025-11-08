n = int(input('введите кол-во строк: '))
m = int(input('введите кол-во столбцов: '))

for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1 or j == 0 or j == m-1:
            print('#', end='')
        else:
            print(' ', end='')
    print()        
