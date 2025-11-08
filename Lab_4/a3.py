while True:
    paketi = input("введите 0 и 1 (не менее 5 символов): ")
    
    if len(paketi) < 5:
        print("cтрока должна содержать не менее 5 символов!")
        continue
    else:
        if not all(char in '01' for char in paketi):
            print("Неверный ввод. Используйте только символы '0' и '1'!")

    paketi.count('0')        

