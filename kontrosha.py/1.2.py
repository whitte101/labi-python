a = (input("введите слово "))
if a.endswith("ь"):
    print(a[-2])
else:
    print(a[-1])    
