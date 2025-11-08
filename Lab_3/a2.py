import string

q = input("введите пароль: ")
a = True

allowed_sym = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
b = ""

if len(q) != 8:
    b = b + 'неверная длина пароля \n'
    a = False

if q.lower() == q:
    b = b + 'нет заглавных букв \n'
    a = False

if q.upper() == q:
    b = b + 'нет строчных букв \n'
    a = False

if not any(map(str.isdigit, q)):
    b = b + 'нет цифр \n'
    a = False

if ('*' not in q) and ('-' not in q) and ('#' not in q):
    b = b + 'нет специальных символов \n'
    a = False

if (set(q) - set(allowed_sym)) != set():
    b = b + 'есть недопустимые символы \n'
    a = False

if a == True:
    print("надежный пароль")
else:
    print("пароль не надежный \n")
    print(b)

