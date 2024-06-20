#задача 1
def show_meteo(temperature, weather):
    print(f'Сейчас {weather}, на градуснике {temperature}.')

show_meteo(24, 'облачно')

#задача 2
for messages_count in range(0, 21):
    if messages_count == 0:
        print(f'У вас нет новых сообщений')
    elif messages_count == 1:
        print(f'У вас 1 новое сообщение')
    elif messages_count <= 4:
        print(f'У вас {messages_count} новых сообщения')
    else:
        print(f'У вас {messages_count} новых сообщений')


#задача 3
def print_time(hour, minute, second):
    print(f'На часах {hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}')

print_time('19', '28', '06')

#задача 4
def calc_stat(listened):
    return f'Вы прослушали {len(listened)} песен.'

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

#задача 5
def calc_stat(listened):
    total_songs = len(listened)
    total_duration = sum(listened)
    return f"Вы прослушали {total_songs} песен общей продолжительностью {total_duration} минут."

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

#задача 6
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
        return f'У тебя {count} друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))

#задача 7
database = {
    'серёга': 'омск',
    'соня': 'москва',
    'миша': 'москва',
    'дима': 'челябинск',
    'алина': 'красноярск',
    'егор': 'пермь',
    'коля': 'красноярск'
}

def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'

def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(database)
        return f'у тебя {format_friends_count(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(database)
        return f'твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(database.values())
        cities_string = ', '.join(unique_cities)
        return f'твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'

print('привет, я анфиса!')
print(process_anfisa('сколько у меня друзей?'))
print(process_anfisa('кто все мои друзья?'))
print(process_anfisa('где все мои друзья?'))
print(process_anfisa('кто виноват?'))

#задача 8
def process_query(query):
    name, question = query.split(', ', 1)
    
    if name == 'анфиса':
        return process_anfisa(question)

def process_anfisa(question):
    if question == 'сколько у меня друзей?':
        return 'У тебя друзей много!'
    elif question == 'кто все мои друзья?':
        return 'Твои друзья: Коля, Соня, Маша'
    elif question == 'где все мои друзья?':
        return 'Коля в городе Красноярск, Соня в Москве, Маша в Питере'
    else:
        return None

print(process_query('анфиса, сколько у меня друзей?'))
print(process_query('анфиса, кто все мои друзья?'))
print(process_query('анфиса, где все мои друзья?'))
print(process_query('анфиса, кто виноват?'))
print(process_query('соня, ты где?'))

#задача 9
DATABASE = {
'Серёга': 'Омск',
'Соня': 'Москва',
'Миша': 'Москва',
'Дима': 'Челябинск',
'Алина': 'Красноярск',
'Егор': 'Пермь',
'Коля': 'Красноярск'
}

# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья" 
# в зависимости от того, какое число передано в аргументе friends_count
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
# Вызовите функцию format_friends_count() и передайте в неё count.
# Отредактируйте строку ниже: в ней должно использоваться выражение, 
# которое вернёт функция format_friends_count()
        return f'У тебя {format_friends_count(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'

def process_query(query):
    elements = query.split(', ')
    name = elements[0]
    if name == 'Анфиса':
        query = query.strip('Анфиса, ')
        return process_anfisa(elements[1])
    else:    
        return process_friend(name, elements[1])  

def process_friend(name, query):
    if name in DATABASE:
        if query == 'ты где?':
            city = DATABASE[name]            
            return f'{name} в городе {city}'
        else:   
            return '<неизвестный запрос>'  
    else:   
            return f'У тебя нет друга по имени {name}'

print('Привет, я Анфиса!')
print(process_anfisa('сколько у меня друзей?'))
print(process_anfisa('кто все мои друзья?'))
print(process_anfisa('где все мои друзья?'))
print(process_anfisa('кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?'))