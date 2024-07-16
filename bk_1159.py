# https://www.acmicpc.net/problem/1159 - using defaultdict
from collections import defaultdict
res = []
all = defaultdict(list)
num = int(input())
for n in range(num):
    name = input()
    all[name[0]].append(name)


for key in all.keys():
    if len(all[key]) >= 5:
        res.append(key)

# need to return in lexicographical order
res.sort()

if res:
    print(''.join(res))
else:
    print("I GIVE UP")