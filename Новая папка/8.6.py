#задача 1
import requests


url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    'T': ''# добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
}

response = requests.get(url, params=weather_parameters)

print(response.text)

#задача 2
import requests

url = 'https://wttr.in'  

weather_parameters = {
    '0': '',
    'T':'',
    'M': '',
    'lang': 'ru'
    
}

response = requests.get(url, params=weather_parameters)  

print(response.text)

#задача 3
import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': ''
}

request_headers = {
    'Accept-Language': 'ru'
}

response = requests.get(url, params=weather_parameters, headers=request_headers)
print(response.text)

#задача 4
import requests


cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    try:
        url = make_url(city)
        params = make_parameters()
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return '<Ошибка на сервере погоды>'
    except requests.ConnectionError:
        return '<Сетевая ошибка>'


print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))