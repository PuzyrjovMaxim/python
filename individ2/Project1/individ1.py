n = int(input())
tree = {}
for i in range(n):
    s = input()
    child, parent = s.split()
    tree[parent] = child

people = set(tree.keys()) | set(tree.values())
numofp = {}

def f(name):
    if name not in tree:
        numofp[name] = 0
        return 0
    ch = tree[name]
    if ch in numofp:
        v = numofp[ch] + 1
    else:
        v = f(ch) + 1
    numofp[name] = v
    return v

for i in people:
    f(i)
sort_num = dict(sorted(numofp.items(), key=lambda x:x[1]))
print(sort_num)
