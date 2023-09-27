# 1 ~ 250  사이의 ㅣ모든 소수를 표시

# 1. python file.py > results.txt
is_sosu = None
def sosu(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

# basic
for num in range(2, 251) :
    if sosu(num) :
        print(num, "은 소수입니다.")
        is_sosu = num

print(is_sosu, " is소수")


# 2. python file.py - file open & write

# 2-1. open & close
# f = open('results.txt', 'wt')
# for num in range(2, 250) :
#     if sosu(num) :
#         print(num, '은 소수입니다.')
#         f.write(f"{num} 은 소수입니다 \n")
# f.close()


# 2-2. with open
# with open('results.txt', 'w') as f:
#     for num in range(2, 251):
#         if sosu(num):
#             print(num, "은 소수입니다.")
#             f.write(f"{num} 은 소수입니다\n")

# print("File Save Successfully")
