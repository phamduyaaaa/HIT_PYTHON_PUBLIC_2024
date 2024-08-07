#B1
my_dict= {
    "SV001": 3.6,
    "SV002": 2.5,
    "SV003": 0.7,
    "SV004": 1.2,
    "SV005": 2.9,
    "SV006": 3.4
}
my_dict["SV007"]= 1.3
my_dict.pop("SV003")
low_score = []
up_score = 0
for MSV,Diem in my_dict.items():
    if Diem<2.0:
        low_score.append(MSV)
    if 3.0<=Diem<=3.5:
        up_score +=1
for MSV in low_score:
    my_dict.pop(MSV)
print(up_score)
print(my_dict)
#B2
import random
def check_count(char,str):
    count = 0
    for i in str:
        if i == char:
            count+=1
    return count
str = input("Str: ")
str = list(str)
value = []
check_str = list(set(str))
for i in check_str:
    value.append(check_count(i,str))
dict_count = {check_str[i]:value[i] for i in range(len(value))}

print(dict_count)
#B3
list = ["CNTT","KHMT", "KTPM","HTTT","RBNT"]
n = int(input("NHap so luong tai khoan sinh vien:"))
dict3 = {f"Account{i}":
            {"Username":f"2023{i:06d}","Password": f"{random.choice(list)}2023{i:06d}"}
        for i in range(n)}
print(dict3)
#B4
dict4 = {"n":1500,
         "m":2,
         "CLUSTERS":3,
         "ITER":10000,
         "METHOD":"FCM",
         "MEASURE":"EUCLIDEAN",
         "YEARS":51}
dict4["MEASURE"]="MANHATAN"
dict4["LOSS FUNCTION"]="NORM_2"
dict4.pop("YEARS")
set4 = []
s = input("S: ")
for value in dict4.items():
    set4.append(value[1])
    if s == str(value[1]):
        print("YES")
set4 =set(set4)
list4 = list(dict4)
print(dict4)
print(list4)
print(set4)
