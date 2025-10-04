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


