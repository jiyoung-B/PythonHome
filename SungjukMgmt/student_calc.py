# student_calc.py

def calc(student) :
    total = student["kor"] + student["eng"] + student["math"]
    avg = total / 3
    grade = None # 다른 언어는 null이라고 한다.
    if 90 <= avg <= 100 : grade = "A"
    elif 80 <= avg < 90 : grade = "B"
    elif 70 <= avg < 80 : grade = "C"
    elif 60 <= avg < 70 : grade = "D"
    else : grade = "F"
    student["total"] = total
    student["avg"] = avg
    student["grade"] = grade