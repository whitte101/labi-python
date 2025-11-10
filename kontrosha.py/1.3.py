a = (input("введите первое число "))
b = (input("введите второе число "))

first_a = a.lstrip('-')[0]
first_b = b.lstrip('-')[0]

if first_a == first_b:
    print("совпадают")
else: 
    print("не совпадают")    
