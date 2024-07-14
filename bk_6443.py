

from itertools import permutations

words = []
res = []
num = int(input())
for n in range(num):
    w = input()
    words.append(w)

for word in words:
    ana = permutations(list(word), len(word))
    inter = (list(set(ana)))
    for w in inter:
        elem = list(w)
        res.append(''.join(elem))

print(res)

res = list(set(res))
res.sort(key = lambda x: (len(x), x))
print(res)

