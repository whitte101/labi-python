
import random
import time

n = int(input("введите количество примеров: "))
correct_answers = 0
total_time = 0
    
for i in range(1, n + 1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_result = a * b
        
    print(f"вопрос {i}/{n}")
        
    while True:
        start_time = time.time()
        try:
            answer = int(input(f"{a} × {b} = "))
            end_time = time.time()
            break
        except ValueError:
            end_time = time.time()
            print("введите целое число")
        
    time_spend = end_time - start_time
    total_time += time_spend
        
    if answer == correct_result:
        correct_answers += 1
        print(f"верно! (время: {time_spend:.1f} сек)")
    else:
        print(f"неверно! правильно: {correct_result} (Время: {time_spend:.1f} sec)")
    
print("\n" + "="*50)
print("СТАТИСТИКА:")
print("="*50)
print(f"общее время: {total_time:.1f} секунд")
print(f"среднее время на вопрос: {total_time/n:.1f} сек")
print(f"правильных ответов: {correct_answers}/{n}")
print(f"процент правильных: {correct_answers/n*100:.1f}%")
