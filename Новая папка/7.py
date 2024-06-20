#1
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

#2

number1 = int(input("Введите 1 число: "))
number2 = int(input("Введите 2 число: "))
number3 = int(input("Введите 3 число: "))

if number1 > number2 and number1 > number3:
    print("Самое большое число: ", number1)
elif number2 > number1 and number2 > number3:
    print("Самое большое число: ", number2)
elif number3 > number1 and number3 > number2:
    print("Самое большое число: ", number3)

#3
number = int(input("Введите число: "))

factorial = number

for i in range(1, number):
    factorial = factorial * i

print(factorial)

#4
number = int(input("Введите целое число больше 1: "))

for i in range(2, int(number ** 0.5) + 1):
    if (number % i) == 0:
        print(f"{number} не является простым числом.")
        break
    else:
        print(f"{number} является простым числом.")
    

#5
number = int(input("введите число от 1 до 10: "))

for i in range(1, 11):
    print(number * i)

#6
string = input("Введите строку: ")

string = string.replace(" ", "").lower()

if string == string[::-1]:
    print("Это палиндром.")
else:
    print("Это не палиндром.")

#7
string = input("Введите строку: ")


string = string.lower()

vowels_count = 0
consonants_count = 0


vowels = "ауоыиэяюёе"

for char in string:
    if char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

print("Количество гласных букв:", vowels_count)
print("Количество согласных букв:", consonants_count)

#8
numbers = [1, 2, 3, 4, 5]

sum = 0


for i in range(len(numbers)):
    sum += numbers[i] 

print("Сумма всех элементов списка:", sum)

#9

n = int(input("Введите число: "))



for i in range(n, 0, -1):
    print(i)

#10
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)