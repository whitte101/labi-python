
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
    
    if (x1 + y1) % 2 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")