li = [1, 'F', 5, 5, 7, 7, 8]
remove_set = {'F', 5}

li = [i for i in li if i not in remove_set]
print(li)
