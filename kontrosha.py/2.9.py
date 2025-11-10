a = (input("введите число: "))

i = 0

while i < len(a):
    digit = a[i]
    if digit != '2' and digit != '5':
        print(digit, end='')
    i += 1    
        