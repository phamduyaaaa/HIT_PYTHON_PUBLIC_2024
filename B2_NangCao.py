#---5---
def check_total(n):
    total = 0
    while n > 0:
        total += (n % 10) ** 3
        n //= 10
    return total
def check_armstrong_3(n):
    return check_total(n) == n
number = int(input("n = "))
for i in range(1, number + 1):
    if check_armstrong_3(i):
        print(i)
#---6---
def is_perfect_number(num):
    # Tính tổng các ước của num (không bao gồm chính nó)
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    # Kiểm tra xem tổng các ước có bằng chính số không
    return sum_of_divisors == num

def print_perfect_numbers(n):
    for i in range(1, n + 1):
        if is_perfect_number(i):
            print(i)

# Nhập số n
number2 = int(input("n = "))
print_perfect_numbers(number2)
