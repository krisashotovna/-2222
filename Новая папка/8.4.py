#задача 1
import random as r

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you(answer):
    return (r.choice(answer))


print(how_are_you(['Норм.', 'Лучше всех :)', 'Ничего, жить буду']))

#задача 2
import datetime as dt

start_time = dt.datetime(2011, 4, 17)  
final_time = dt.datetime(2019, 4, 15)  

duration = final_time - start_time  
    
print(duration)

#задача 3
import datetime as dt

start_moment = dt.datetime(2019, 11, 16, 12, 0)  
current_moment = dt.datetime(2019, 11, 21, 14, 50)  

total_time = current_moment - start_moment 

print(total_time)

#задача 4
import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(city):
   
    time_in_city = dt.timedelta(hours=UTC_OFFSET [city]) + dt.datetime.utcnow()
    return time_in_city

print(what_time('Екатеринбург'))

#задача 5
import datetime as dt
DATABASE = {
'Серёга': 'Омск',
'Соня': 'Москва',
'Дима': 'Челябинск',
'Алина': 'Красноярск',
'Егор': 'Пермь'
}
UTC_OFFSET = {
'Санкт-Петербург': 3,
'Москва': 3,
'Самара': 4,
'Новосибирск': 7,
'Екатеринбург': 5,
'Нижний Новгород': 3,
'Казань': 3,
'Челябинск': 5,
'Омск': 6,
'Ростов-на-Дону': 3,
'Уфа': 5,
'Красноярск': 7,
'Пермь': 5,
'Воронеж': 3,
'Волгоград': 4,
'Краснодар': 3,
'Калининград': 2
}
def what_time(friend):
    utc_time = dt.datetime.utcnow()
    city = DATABASE[friend]
    a=UTC_OFFSET[city]
    san=utc_time + dt.timedelta(hours=a)
    san.strftime('%H %M')
    return san
print(what_time('Соня'))

#задача 6
import datetime as dt
DATABASE = {
'Серёга': 'Омск',
'Соня': 'Москва',
'Дима': 'Челябинск',
'Алина': 'Красноярск',
'Егор': 'Пермь'
}
UTC_OFFSET = {
'Санкт-Петербург': 3,
'Москва': 3,
'Самара': 4,
'Новосибирск': 7,
'Екатеринбург': 5,
'Нижний Новгород': 3,
'Казань': 3,
'Челябинск': 5,
'Омск': 6,
'Ростов-на-Дону': 3,
'Уфа': 5,
'Красноярск': 7,
'Пермь': 5,
'Воронеж': 3,
'Волгоград': 4,
'Краснодар': 3,
'Калининград': 2
}
def what_time(friend):
    utc_time = dt.datetime.utcnow()
    city = DATABASE[friend]
    a=UTC_OFFSET[city]
    san=utc_time + dt.timedelta(hours=a)
    san.strftime('%H %M')
    return san
print(what_time('Соня'))

#задача 7
import datetime as dt

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city in UTC_OFFSET: return f'Там сейчас {what_time(city)}'
            else:
                return f'<не могу определить время в городе {DATABASE [name]}>'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


def process_query(query):
    tokens = query.split(', ')
    name = tokens[0]
    if name == 'Анфиса':
        return process_anfisa(tokens[1])
    else:
        return process_friend(name, tokens[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?'
    ]
    for query in queries:
        print(query, '-', process_query(query))


runner()
