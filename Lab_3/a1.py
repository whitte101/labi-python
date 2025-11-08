x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

if x1 == 0 or y1 == 0 or x2 == 0 or y2 == 0:
    print("координата не может быть равна 0")
else:
    if x1 > 0:
        if y1 > 0:
            quarter1 = 1
        else:
            quarter1 = 4
    else: 
        if y1 > 0:
            quarter1 = 2
        else:
            quarter1 = 3

quarter2 = 0
if x2 > 0: 
    if y2 > 0:     
         quarter2 = 1
    else:     
        quarter2 = 4
else: 
    if y2 > 0:
        quarter2 = 2
    else:
        quarter2 = 3

if quarter1 == quarter2:
    print(f"обе точки лежат в {quarter1} четверти")
else:
    print("точки лежат в разных четвертях")




