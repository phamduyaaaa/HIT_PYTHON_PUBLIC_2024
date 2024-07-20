#---1---
#--a
number = int(input("Nhap 1 so nguyen duong: "))
total = int(number%10)
while number>0:
    number = int(number/10)
    total += number%10
print(total)
--b
number = int(input("Nhap 1 so nguyen duong: "))
total = 0
for i in range(number):
    if(number%(i+1)==0):
        total += (i+1)
        print(i+1)

print("Tong gia tri cac uoc: %s."%(total))
--c
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
check_can = ""
check_vuong = ""
check_deu = ""
check_goc=""
if(a+b>c and a+c>b and b+c>a):
    if a == b == c:
        check_deu ="deu"
    elif(a == b or b == c or a == c):
        check_can = "can"
    elif(a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2):
            check_vuong = "vuong"
    else:
        goc1 = (math.acos((b**2+c**2-a**2)/(2*b*c))*180)/math.pi
        goc2 = (math.acos((c**2+a**2-b**2)/(2*c*a))*180)/math.pi
        goc3 = (math.acos((a**2+b**2-c**2)/(2*b*a))*180)/math.pi
        if max(goc1,goc2,goc3)<90:
            check_goc="nhon"
        else:
            check_goc="tu"
    print(f"Tam giac {check_vuong}{check_can}{check_deu}{check_goc}")
else:
    print("Khong phai tam giac")
#---2---
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a // b =", a // b)
print("a ** b =", a ** b)
print("a % b =", a % b)
if a > b:
    print("a lớn hơn b")
elif a < b:
    print("a nhỏ hơn b")
else:
    print("a bằng b")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("NOT a == b:", not (a == b))
print("a >> 1 =", a >> 1)
print("a << 1 =", a << 1)
