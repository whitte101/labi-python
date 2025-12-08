def func():
    lst = ['blue', 'hello', 'elemadasents']
    max_len = 0
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
    return max_len
print(func())    