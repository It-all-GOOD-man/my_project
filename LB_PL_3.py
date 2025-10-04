# Задание 1
print("Задание 1")
print([i**2 for i in range(1, 11)])

# Задание 2
print("Задание 2")
print([i for i in range(2, 21, 2)])

# Задание 3
print("Задание 3")
words = ["python", "Java", "C++", "Rust", "go"]
print([i.upper() for i in words if len(i)>3])

# Задание 4
print("Задание 4")
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for i in Countdown(5):
    print(i)
    
# Задание 5
print("Задание 5")
def fibonacci(n):
    a, b = 0, 1
    k = 0
    while k < n:
        yield a
        a = b
        b = a + b
        k += 1
for i in fibonacci(5): print(i)

# Задание 6

from decimal import Decimal, getcontext

getcontext().prec = 10
def fin_calc(summ, procent , years):
    final_amount = summ*(Decimal("1") + procent/(Decimal("12")*Decimal("100")))**(Decimal("12")*years)
    final_amount = final_amount.quantize(Decimal('0.01'))
    prof = final_amount - summ
    return prof
# print(fin_calc(summ=Decimal(input("Введите начальную сумму вклада ")),
                # procent=Decimal(input("Введите процентуню ставку ")), years=Decimal(input("Введите срок вклада в годах "))))

# Задание 7

from fractions import Fraction

f1 = Fraction(3, 4)
f2 = Fraction(5, 6)
print(f"{f1} + {f2} = {f1 + f2} \n"
      f"{f1} - {f2} = {f1-f2} \n"
      f"{f1} * {f2} = {f1*f2} \n"
      f"{f1} / {f2} = {f1/f2}")

# Задание 8
from datetime import datetime, date
n = datetime.now()

print(f"Текущая дата и время: {n}")
print(f"Только текущая дата: {n.date()}")
print(f"Только текущее время: {n.time()}")

# Задание 9

birthday = date(year=int(input("Введите год рождения ")),
                month=int(input("Введите месяц рождения ")),
                day=int(input("Введите день рождения")))
print(birthday)
today = date.today()
next_bd = date(today.year, birthday.month, birthday.day)
if next_bd < today:
    next_bd = date(today.year + 1, birthday.month, birthday.day)
print(f"День рождения: {birthday}")
print(f"Сегодня: {today}")
print(f"Дней прошло с рождения: {(today-birthday).days}")
print(f"Дней до следующего дня рождения: {(next_bd-today).days}")

# Задание 10

def format_date(today:datetime):
    russion_format = {1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"}
    return f"Сегодня {today.day} {russion_format[today.month]} {today.year} года, время: {today.strftime('%H:%M')}"
print(format_date(datetime.now()))

print("Bobby")