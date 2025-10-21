import random
import time

while True:
    try:
        n = int(input("Введите количество примеров: "))
        if n <= 0:
            print("Ошибка: введите положительное число.")
            continue
        break
    except ValueError:
        print("Ошибка: введите целое число.")

correct = 0
total_time = 0.0
times = []

for i in range(n):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answ = a * b
    
    print(f"\nВопрос {i+1}/{n}")
    start_time = time.time()
    
    while True:
        print(f"{a} × {b} = ", end='')
        user_input = input().strip()
        
        if user_input.isdigit():
            user_answer = int(user_input)
            break
        else:
            print("Пожалуйста, введите целое число!")
    
    end_time = time.time()
    time_taken = end_time - start_time
    times.append(time_taken)
    total_time += time_taken
    
    if user_answer == answ:
        correct += 1
        print(f"Верно! (Время: {time_taken:.1f} сек)")
    else:
        print(f"Неверно! Правильно: {answ} (Время: {time_taken:.1f} сек)")

average_time = total_time / n
percentage = (correct / n) * 100

print("\n==================================================")
print("                 СТАТИСТИКА:")
print("==================================================")
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {average_time:.1f} сек")
print(f"Правильных ответов: {correct}/{n}")
print(f"Процент правильных: {percentage:.1f}%")
