a = 'CДП-ПИ-232 (1 курс)'

count = 0
i = 0

while i < len(a):
    if a[i].isdigit():
        count +=1
    i += 1
print(f'кол-во символов = {count}')    