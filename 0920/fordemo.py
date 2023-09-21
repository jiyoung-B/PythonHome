# 1, 2, 3, 4, 5
# list_ = [1,2,3,4,5]

for num in range(1, 10, 2):
            # range(초기값, 끝값+1, 증감값)
            # 초기값 0은 생략, 증감값 1 이면 생략
    print(num, end = '\t')
print()
print()

# 1단계 1부터 100까지 출력해본다.
for num in range(1, 101):
    print(num, end = '\t')
print()
print()

# 2단계 7의 배수만 찍는다. - 반복문 안에 조건문
for num in range(1, 101):
    if num % 7 == 0:
        print(num, end = '\t')
print()
print()

# 3단계 2의 결과를 한줄에 5개씩 찍는다
count = 0
for num in range(1, 101):
    if num % 7 == 0:
        print(num, end = '\t')
        count +=1
        if count % 5 == 0 :
            print() # 줄바꾸기
print()
