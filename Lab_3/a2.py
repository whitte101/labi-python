import string

password = input("введите пароль: ")
a = True

allowed_sym = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
b = ""

if len(password) != 8:
    b = b + 'неверная длина пароля \n'
    a = False

if password.lower() == password:
    b = b + 'нет заглавных букв \n'
    a = False

if password.upper() == password:
    b = b + 'нет строчных букв \n'
    a = False

if not any(map(str.isdigit, password)):
    b = b + 'нет цифр \n'
    a = False

if ('*' not in password) and ('-' not in password) and ('#' not in password):
    b = b + 'нет специальных символов \n'
    a = False

if (set(password) - set(allowed_sym)) != set():
    b = b + 'есть недопустимые символы \n'
    a = False

if a == True:
    print("надежный пароль")
else:
    print("пароль не надежный \n")
    print(b)

