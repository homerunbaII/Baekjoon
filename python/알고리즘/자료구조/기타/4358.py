import sys

tree_list = {}
cnt = 0


while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    cnt += 1
    if tree in tree_list:
        tree_list[tree] += 1
    else:
        tree_list[tree] = 1

tree_sortlist = dict(sorted(tree_list.items()))

for tree in tree_sortlist:
    print('{0} {1:.4f}'.format(tree, tree_sortlist[tree] / cnt * 100))
