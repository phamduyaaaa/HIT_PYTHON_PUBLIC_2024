#B1
check = lambda a,b: a if ord(a)>ord(b) else b
a = input("a: ")
b = input("b: ")
print(check(a,b))
#B2
def transposition_matrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transposed.append(row)
    return transposed
n = int(input("Số hàng: "))
m = int(input("Số cột: "))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        k = input(f"Phần tử tại vị trí ({i + 1},{j + 1}): ")
        row.append(k)
    matrix.append(row)
print("Ma trận ban đầu:")
for row in matrix:
    print(row)
transposed_matrix = transposition_matrix(matrix)
print("Ma trận chuyển vị:")
for row in transposed_matrix:
    print(row)
#3
def calculate(*args,operation):
    result = 0
    if operation =="add":
        for i in args:
            result +=i
    elif operation =="multiply":
        for i in args:
            result *=i
    elif operation =="max":
        result =  max(args)
    elif operation=="min":
        result = min(args)
    return result

a = calculate(1,2,3,4,operation="min")
print(a)
#4
def len_number(number:int):
    cnt =1
    while(number>10):
        cnt+=1
        number/=10
    return cnt
def sum_number(number:int):
    total = 0
    cnt = len_number(number)
    while cnt>0:
        cnt-=1
        total += number%10
        number //=10
    return total
print(len_number(12345))
print(sum_number(12345))
#5
def format_phone_number(phone_number):
    digits =''.join(filter(str.isdigit,phone_number))

    if len(digits) !=10 or not digits.startswith('0'):
        return "Ivalid phone number"
    return "+84" + digits[1:]
print(format_phone_number("0983-765-432"))
