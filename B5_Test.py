#B1
def check_count(a,tuple):
    count = 0
    for i in tuple:
        if i == a:
            count +=1
    return count
# n = int(input("So luong phan tu:"))
# tuple =[]
# for i in range(1,n+1):
#     a = int(input(f"Phan Tu {i}: "))
#     tuple.append(a)
# set = set(tuple)
# for i in set:
#     if (check_count(i,tuple)%5==0 and check_count(i,tuple)%2!=0):
#         print(i)
#B2
# goal = int(input("GOAL POSITION(1->1000): "))
# print(round((goal/3)+1/2))
#B3
# list_names=[]
# list_scores=[]
# members = int(input("INT"))
# max_score = 0
# for i in range(1,members+1):
#     key = str(input(f"Name {i}: "))
#     value = int(input(f"Score {i}: "))
#     list_names.append(key)
#     list_scores.append(value)
#     if (value>=max_score):
#         max_score = value
#         tier = key
# print(tier)
#B4
# list4 = input()
# print(len(list4))
# print(list4)
# list_new = []
# for i in list4:
#     if i == "[" or i ==']' or i ==',' or i==" " or i=="“" or i=="”":
#         continue
#     else:
#         list_new.append(i)
# list_new = set(list_new)
# list_new =list(list_new)
# print(list_new)
#B5
def check1(list):
    for i in list:
        if i<0:
            return False
            break
        else:
            continue
    return True
def check2(list):
    if len(list) != len(set(list)):
        return False
    else:
        return True
def check3(list1):
    listcheck = list1.copy()
    list1.sort()
    for i in range(0,len(list1)):
        if listcheck[i] != list1[i]:
            return False
            break
        else:
            continue
    return True

# n = int(input())
# list5 = []
# for i in range(n):
#     list5.append(int(input()))
# check1 = check1(list5)
# check2 = check2(list5)
# check3 = check3(list5)
# if check1 and check2 and check3:
#     print(max(list5)+1)
