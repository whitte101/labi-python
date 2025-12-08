def func(a, b):
    result = ""
    for char in a:
        if char not in b:
            result += char
    return result    

d = input('1 stroka: ')
c = input('2 stroka: ')

print (func(d, c))