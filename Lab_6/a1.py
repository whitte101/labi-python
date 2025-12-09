import xml.etree.ElementTree as ET
from collections import defaultdict, Counter
import os

def load_users_data(path):
    users = []
    tree = ET.parse(path)
    root = tree.getroot()
    for u in root.findall('user'):
        users.append({
            'user_id': int(u.find('user_id').text),
            'name': u.find('name').text,
            'age': int(u.find('age').text),
            'weight': int(u.find('weight').text),
            'fitness_level': u.find('fitness_level').text,
            'workouts': []
        })
    return users

def load_workouts_data(path):
    workouts = []
    tree = ET.parse(path)
    root = tree.getroot()
    for w in root.findall('workout'):
        workouts.append({
            'workout_id': int(w.find('workout_id').text),
            'user_id': int(w.find('user_id').text),
            'date': w.find('date').text,
            'type': w.find('type').text,
            'duration': int(w.find('duration').text),
            'distance': float(w.find('distance').text),
            'calories': int(w.find('calories').text),
            'avg_heart_rate': int(w.find('avg_heart_rate').text),
            'intensity': w.find('intensity').text
        })
    return workouts

def attach_workouts_to_users(users, workouts):
    user_map = {u['user_id']: u for u in users}
    for w in workouts:
        user_map[w['user_id']]['workouts'].append(w)
    return users

def get_stats(users, workouts):
    return {
        'total_workouts': len(workouts),
        'total_users': len(users),
        'total_calories': sum(w['calories'] for w in workouts),
        'total_time_hours': sum(w['duration'] for w in workouts) / 60.0,
        'total_distance': sum(w['distance'] for w in workouts)
    }

def analyze_user_activity(users):
    result = []
    for u in users:
        ws = u['workouts']
        result.append({
            'name': u['name'],
            'fitness_level': u['fitness_level'],
            'workouts_count': len(ws),
            'total_calories': sum(w['calories'] for w in ws),
            'total_time_h': sum(w['duration'] for w in ws) / 60.0
        })
    result_sorted = sorted(result, key=lambda x: (x['workouts_count'], x['total_calories']), reverse=True)

    print("\nТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for i, r in enumerate(result_sorted[:3], start=1):
        print(f"  {i}. {r['name']} ({r['fitness_level']}):")
        print(f"   Тренировок: {r['workouts_count']}")
        print(f"   Калорий: {r['total_calories']}")
        print(f"   Время: {r['total_time_h']:.1f} часов\n")
    return result_sorted

def analyze_workout_types(workouts):
    total = len(workouts)
    by_type = defaultdict(list)
    for w in workouts:
        by_type[w['type']].append(w)

    print("\nРАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for t in sorted(by_type):
        lst = by_type[t]
        cnt = len(lst)
        pct = cnt / total * 100
        avg_dur = sum(w['duration'] for w in lst) / cnt
        avg_cal = sum(w['calories'] for w in lst) / cnt
        print(f"  {t.capitalize()}: {cnt} тренировок ({pct:.1f}%)")
        print(f"    Средняя длительность: {avg_dur:.0f} мин")
        print(f"    Средние калории: {avg_cal:.0f} ккал")

def find_user_workouts(users, user_name):
    user = next((u for u in users if u['name'].lower() == user_name.lower()), None)
    if user is None:
        return None, []
    return user, user['workouts']

def analyze_user(user, workouts):
    n = len(workouts)
    total_cal = sum(w['calories'] for w in workouts)
    total_time_h = sum(w['duration'] for w in workouts) / 60.0
    total_distance = sum(w['distance'] for w in workouts)
    avg_cal = round(total_cal / n) if n else 0
    fav = Counter(w['type'] for w in workouts).most_common(1)
    fav_type = fav[0][0] if fav else "—"

    print(f"\nДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user['name']}")
    print("=" * 40)
    print(f"Возраст: {user['age']} лет, Вес: {user['weight']} кг")
    print(f"Уровень: {user['fitness_level']}")
    print(f"Тренировок: {n}")
    print(f"Сожжено калорий: {total_cal}")
    print(f"Общее время: {total_time_h:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")
    print(f"Средние калории за тренировку: {avg_cal}")
    print(f"Любимый тип тренировки: {fav_type}")

def main():
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    users = load_users_data(os.path.join(downloads, 'users.xml'))
    workouts = load_workouts_data(os.path.join(downloads, 'workouts.xml'))

    users = attach_workouts_to_users(users, workouts)
    stats = get_stats(users, workouts)

    print("ОБЩАЯ СТАТИСТИКА")
    print("===========================")
    print(f"Всего тренировок: {stats['total_workouts']}")
    print(f"Всего пользователей: {stats['total_users']}")
    print(f"Сожжено калорий: {stats['total_calories']}")
    print(f"Общее время: {stats['total_time_hours']:.1f} часов")
    print(f"Пройдено дистанции: {stats['total_distance']:.1f} км")

    analyze_user_activity(users)
    analyze_workout_types(workouts)

    user, ws = find_user_workouts(users, "Борис")
    analyze_user(user, ws)

if __name__ == "__main__":
    main()
