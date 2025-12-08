a = (input("Enter a number: "))
b = (input("Enter a number: "))

c = a.lstrip('-')[0]
d = b.lstrip('-')[0]

if c == d:
    print('da')
else:
    print('net')     