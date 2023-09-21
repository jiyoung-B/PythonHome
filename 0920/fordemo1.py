count = 0
for i in range(65, 91) :  # 65 ~ 90 
    print(chr(i), end='\t')
print()

for i in range(97, 123) : # 97 ~ 122
    print(chr(i), end='\t')
print()


for num in range(1, 101):
    if num % 7 == 0:
        print(num, end = '\t')
        count +=1
        if count % 5 == 0 :
            print() # 줄바꾸기
print()

# # 65 + 32 = 97
# A       B       C       D       E
# f       g       h       i       j
# K       L       M       N       O
# p       q       r       s       t
# U       V       W       X       Y
# z
count = 0
line = 1
for i in range(65, 91) :
    if line % 2 == 1 : print(chr(i), end = '\t')
    else : print(chr(i+32), end ='\t')
    count += 1
    if count % 5 == 0 :
        print()
        line +=1
print()