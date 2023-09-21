# score = int(input("Enter a Score : "))
# if score >= 60 :
#     print("Success")
# else :
#     print("Failure")


avg = int(input("Enter a Average : "))
if 90 <= avg <= 100 : print("A")
elif 80 <= avg < 90 : print("B")
elif 70 <= avg < 80 : print("C")
elif 60 <= avg < 70 : print("D")
else : print("F")

season = input("Favorite Season?").lower() # 소문자로 바꿔 입력
if season == "spring" :
    print("개나리, 진달래")
elif season == "summer" :
    print("장미, 아카시아")
elif season == "fall" :
    print("코스모스, 백합")
else :
    print("동백, 매화")

