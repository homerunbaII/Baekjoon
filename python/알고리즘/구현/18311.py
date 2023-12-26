n , k = map(int, input().split())
course = list(map(int,input().split()))

course_length = []
course_sum = 0
for i in range(n):
    course_sum += course[i]
    course_length.append(course_sum)

revese_course_length = []

course_sum = 0
for i in range(n):
    course_sum += course[n - 1 - i]
    revese_course_length.append(course_sum)

if k >= course_length[-1]:
    reverse_length = k - course_length[-1]
    for i in range(n):
        if reverse_length < revese_course_length[i]:
            print(n -i)
            break
else:
    for i in range(n):
        if k < course_length[i]:
            print(i + 1)
            break

    


# for i in range(n)
# length = sum(course)

# acc_length = 0

# if k >= length:
#     for i in range(n):
#         acc_length += i

#         if 
# else:
#     pass