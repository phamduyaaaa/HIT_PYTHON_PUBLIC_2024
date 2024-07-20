#---7---
def sum_of_divisors(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total
def find_amicable_pairs(n):
    amicable_pairs = set()
    for i in range(1, n + 1):
        j = sum_of_divisors(i)
        if j > i and j <= n:
            if sum_of_divisors(j) == i:
                amicable_pairs.add((i, j))
    return amicable_pairs
number = int(input("n = "))
pairs = find_amicable_pairs(number)
for pair in pairs:
    print(pair)
# ---8---
n = int(input("n= "))
i = 1
all_rows = []

while i<=n:
    row=[1]*i
    if i>=3:
        for j in range(1,i-1):
            row[j] = all_rows[i-2][j-1]+all_rows[i-2][j]
    all_rows.append(row)
    print(row)
    i+=1
#---9---
a = int(input("Nhập số a: "))
bits = 0
if a < 0:
    print("Error")
elif a == 0:
    print(0)
else:
    while a>0:
        a>>=1
        bits+=1
    print(bits)
x = "awesome"
print("Python is",x)
print(f"Python is {x}")
print("Python is %s"%(x))
