n = int(input("ведите кол-во строк (n): "))
m = int(input("введите кол-во столбцов (m): "))

print("Прямоугольник:")
for i in range(n):
    for j in range(m):
        print("#", end="")
    print()  