import math

total_grade = 0
total_lec = 0
dic = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0 , 'F' : 0}

for i in range(20):
    lec, per, grade = input().split()
    per = float(per)
    if grade == 'P':
        continue
    total_grade += (dic[grade] * per)
    total_lec += per

print(total_grade/total_lec)
