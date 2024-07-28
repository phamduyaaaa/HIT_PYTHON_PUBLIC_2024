#B1:
N = int(input("Nhập số phần tử của list: "))
my_list = []
for i in range(N):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    my_list.append(x)
X = int(input("Nhập số X cần kiểm tra: "))
so_lan_xuat_hien = my_list.count(X)
print(f"Số lần {X} xuất hiện trong list: {so_lan_xuat_hien}")
my_list[1:7] = [8, 5, 4, 0, 1, 3]
max_value = max(my_list)
min_value = min(my_list)
print(f"Số lớn nhất trong list: {max_value}")
print(f"Số nhỏ nhất trong list: {min_value}")
Y = int(input("Nhập số Y cần chèn vào đầu list: "))
my_list.insert(0, Y)
sorted_list = sorted(my_list)
if my_list == sorted_list:
    print("TĂNG")
elif my_list == sorted_list[::-1]:
    print("GIẢM")
else:
    print("NO")
new_list = [sum(my_list[:i+1]) for i in range(N)]
list_1 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
sorted_list_normal = sorted(list_1)
sorted_list_absolute = sorted(list_1, key=abs)
print("List mới sau khi sắp xếp tăng dần:", sorted_list_normal)
print("List mới sau khi sắp xếp tăng dần theo giá trị tuyệt đối:", sorted_list_absolute)
#B2
a = []
k = int(input("Nhập số phần tử của danh sách a: "))
for i in range(k):
    x = int(input(f"Nhập phần tử thứ {i+1} của danh sách a: "))
    a.append(x)
n = int(input("Nhập số dòng của ma trận: "))
m = int(input("Nhập số cột của ma trận: "))
if n * m <= k:
    X = [a[i*m: (i+1)*m] for i in range(n)]
    for row in X:
        print(row)
else:
    print("NO")
#B3
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")
print("Chuỗi s1 sau khi đảo ngược:", s1[::-1])
a = int(input("Nhập số nguyên a (1 <= a): "))
b = int(input(f"Nhập số nguyên b ({a} < b <= {len(s2)}): "))
reversed_part = s2[a-1:b][::-1]
result_s2 = s2[:a-1] + reversed_part + s2[b:]
print("Chuỗi s2 sau khi đảo ngược từ vị trí", a, "đến vị trí", b, ":", result_s2)
s3 = s1[::2]
print("Chuỗi s1 sau khi xóa các kí tự vị trí chẵn:", s3)
s4 = ''.join(''.join(x) for x in zip(s1, s2))
print("Chuỗi s4 đan xen từ s1 và s2:", s4)
swapped_s1 = s2[:2] + s1[2:]
swapped_s2 = s1[:2] + s2[2:]
print("Chuỗi s1 sau khi đổi chỗ 2 ký tự đầu với chuỗi s2:", swapped_s1)
print("Chuỗi s2 sau khi đổi chỗ 2 ký tự đầu với chuỗi s1:", swapped_s2)
#B4
def chuan_hoa_ho_ten(s):
    s = s.lower()
    words = s.split()
    words = [word.capitalize() for word in words]
    return ' '.join(words)
ho_ten = input("Nhập chuỗi họ tên cần chuẩn hóa: ")
print("Chuỗi họ tên sau khi chuẩn hóa:", chuan_hoa_ho_ten(ho_ten))
