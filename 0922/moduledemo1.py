import calendar, random
from datetime import datetime
# print(calendar.month(2023, 9)) 
# print(calendar.calendar(2023)) 
print(datetime.now())
count = 1
result = []
for i in range(1, 7) :
    print(random.randint(1, 45))
    ran = random.randint(1, 45)
    count += 1
    result.append(ran)
    if count >= 7 :
        print(result)
