n = int(input())
directory = input()
directory = list(directory)
for i in range(n-1):
    directory_new = input()
    directory_new = list(directory_new)
    for j in range(len(directory_new)):
        if directory[j] == directory_new[j]:
            pass
        else:
            directory[j] = '?'

print(''.join(directory))