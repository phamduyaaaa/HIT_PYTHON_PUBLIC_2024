import math
#---3---
#--a
n = int(input("Nhap n: "))
result = 0
for i in range(2*n+1):
    if (i+1)%2==0:
        result-=(i+1)
    else:
        result+=(i+1)
print(result)
--b
n = int(input("Nhap n: "))
result = 0
for i in range(n):
    result += 1/(i+1)
print(result)
--c
def bien_luan_nghiem(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm.")
            else:
                print("Phương trình vô nghiệm.")
        else:
            x = -c / b
            print(f"Phương trình có một nghiệm: x = {x}")
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm.")
        elif delta == 0:
            x = -b / (2*a)
            print(f"Phương trình có nghiệm kép: x = {x}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
bien_luan_nghiem(a, b, c)
# Test:
# Ví dụ 1: Phương trình có vô số nghiệm (0,0,0)
# Ví dụ 2: Phương trình vô nghiệm (0,0,1)
# Ví dụ 3: Phương trình có một nghiệm (0,2,-4)
# Ví dụ 4: Phương trình bậc hai vô nghiệm (1,2,5)
# Ví dụ 5: Phương trình có nghiệm kép (1,-2,1)
# Ví dụ 6: Phương trình có hai nghiệm phân biệt (1,-3,2)
#---4---
def fibonaci(n):
    a = []
    n0 = 0
    n1 = 1
    for i in range(n):
        if(i==0):
            a.append(n0)
        elif(i==1):
            a.append(n1)
        else:
            a.append(a[i-1]+a[i-2])
    return a[n-1]
print(fibonaci(10))
