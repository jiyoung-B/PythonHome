def calc_sum(start, end): # Parameter, 매개변수
    sum = 0
    for i in range(start, end + 1):
        sum += i
    
    return sum # sum의 값을 가지고 복귀.(함수는 복귀한다)
    # ==
    # print('%d부터 %d까지의 합은 %d 입니다.' %(start,end,sum))
    # return


start = 50
end = 70
# calc_sum(start, end) # 인자, 인수, Argument, Call by Value
# print('%d부터 %d까지의 합은 %d 입니다.' %(start,end,calc_sum(start, end))) # 가져온 함수를 프린트
# 보통 result 로 받아.
result = calc_sum(start, end)
