print(f"Вероятность выигрыша для игрока, оставшегося при своем первоначальном выборе: {prob_player1_no_change:.4f}")
print(f"Вероятность выигрыша для игрока, не меняющего свой выбор: {prob_player2_no_change:.4f}")
print(f"Вероятность выигрыша для игрока, меняющего свой выбор: {prob_player2_change:.4f}")


# ЗАДАНИЕ 5
import random

# Списки предметов разных редкостей
common_items = ["Обычный предмет 1", "Обычный предмет 2", "Обычный предмет 3"]
rare_items = ["Редкий предмет 1", "Редкий предмет 2"]
epic_items = ["Эпический предмет 1", "Эпический предмет 2"]
legendary_items = ["Легендарный предмет 1"]

# Шансы на выпадение предметов
chances = {
    "common": 0.7,
    "rare": 0.2,
    "epic": 0.1,
    "legendary": 0.05
}

# Счетчики выпавших предметов
counts = {
    "common": 0,
    "rare": 0,
    "epic": 0,
    "legendary": 0
}

# Открытие лутбоксов
lootbox_count = 20
items = []

for _ in range(lootbox_count):
    rand = random.random()
    if rand < chances["common"]:
        item = random.choice(common_items)
        counts["common"] += 1
    elif rand < chances["common"] + chances["rare"]:
        item = random.choice(rare_items)
        counts["rare"] += 1
    elif rand < chances["common"] + chances["rare"] + chances["epic"]:
        item = random.choice(epic_items)
        counts["epic"] += 1
    else:
        item = random.choice(legendary_items)
        counts["legendary"] += 1
    items.append(item)

# Проверка условий
luck_message = ""
if counts["epic"] > 3:
    luck_message = " (Удача!)"
if counts["legendary"] > 1:
    luck_message = " (Большая удача!)"

# Вывод результатов
print(f"Обычные предметы: {counts['common']}")
print(f"Редкие предметы: {counts['rare']}")
print(f"Эпические предметы: {counts['epic']}")
print(f"Легендарные предметы: {counts['legendary']}")
print(luck_message)

# Отображение полученных предметов разного цвета
for item in items:
    if item in common_items:
        print(f"\033[0m{item}")  # белый цвет
    elif item in rare_items:
        print(f"\033[34m{item}")  # синий цвет
    elif item in epic_items:
        print(f"\033[35m{item}")  # фиолетовый цвет
    else:
        print(f"\033[33m{item}")  # оранжевый цвет