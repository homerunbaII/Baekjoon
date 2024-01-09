n , erase = map(int, input().split())
number = input()

start = int(number[0 : n - erase])
print(start)
i = 1
while i < n - erase - 1:
    if start <= int(number[i: n - erase + i]):
        start = int(number[i: n - erase + i])
        i += 1
        print(start)
        continue
    else: 
        str_start = str(start)
        j = 0
        print(str_start[j: n - erase])
        while  j  < n - erase:
            if  int(str_start[j: n - erase]) < int(number[i + j: n - erase + i]):
                start = int(str_start[0 : j] + number[i + j : n - erase + i])
                break
            else:
                j += 1
        i += 1
        
print(start)


# 52439167825
# 524
# 243 543
# 439 549
# 391 5
# 916
# 167, -> 917
# 678 -? 978
# 782
# 825