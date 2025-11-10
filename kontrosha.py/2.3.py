n = int(input("введите число N:"))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print() 
