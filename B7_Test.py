#1
str1 = input()
char1 = list(str1)
for i in char1:
    if not i.isdigit():
        a = str1.split(i)
for i in a:
    total = 0
    if i.isdigit():
        total += int(i)
print(total)

#2
def cal_total_number(number):
    total = 0
    l = list(str(number))
    for i in l:
        total += int(i)
    if total == 10:
        return True
    else:
        return False
def perfect_numbers(index):
    start = 19
    list_perfect_numbers = []
    while(len(list_perfect_numbers)!=index):
        if cal_total_number(start):
            list_perfect_numbers.append(start)
        start+=1
    return list_perfect_numbers[index-1]

print(perfect_numbers(11))
#3
class Vehicle:
    def __init__(self,made):
        self.made = made
    def description(self):
        pass
class Car(Vehicle):
    def __init__(self,made,model):
        super().__init__(made)
        self.model = model
    def description(self):
        print(f"Made in {self.made} - Model: {self.model}")
class ElectricCar(Car):
    def __init__(self,made,model,battery_size):
        super().__init__(made,model)
        self.battery_size = battery_size
    def description(self):
        print(f"Made in {self.made} - Model: {self.model} - Battery size: {self.battery_size}")

vinf = ElectricCar("VN","f9",40000)
vinf.description()
#4
class TamThucBacHai:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        print(f"{a}x2+{b}x+{c}")
    def __add__(self, other):
        return TamThucBacHai(self.a + other.a, self.b + other.b, self.c + other.c)
    def __sub__(self, other):
        return TamThucBacHai(self.a - other.a, self.b - other.b, self.c - other.c)
a = TamThucBacHai(1,2,3)
b = TamThucBacHai(4,5,6)

print(f"a = {a.__sub__(b).a};b = {a.__sub__(b).b};c = {a.__sub__(b).c}")
