#задача 1
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Проверяем, если запрос о друзьях
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        for friend in DATABASE.keys():
            friends_string += friend + ' '
        return 'Твои друзья: ' + friends_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))






#задача 2
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Проверяем, если запрос о друзьях
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        for friend in DATABASE.keys():
            friends_string += friend + ' '
        return 'Твои друзья: ' + friends_string
    # Проверяем, если запрос о городах друзей
    elif query == 'Где все мои друзья?':
        return 'Я поняла, это вопрос про города!'
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))



#задача3
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Проверяем, если запрос о друзьях
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        for friend in DATABASE.keys():
            friends_string += friend + ' '
        return 'Твои друзья: ' + friends_string
    # Проверяем, если запрос о городах друзей
    elif query == 'Где все мои друзья?':
        cities = set(DATABASE.values())
        cities_string = ' '.join(cities)
        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'

print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))