a = 'abcdefABCDEF'
i = 0
result = ''

while i < len(a):
    if a[i].islower(): 
        result += a[i] + ' '
    i += 1

print(result.strip())        