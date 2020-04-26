import math

list1 = [-4, -1, 0, 55, 10, 21]

l = []
# [math.pow(i,2) for i in list1 if math.pow(i,2)>=0]
for i in list1:
    if math.pow(i, 2) >= 0:
        l.append(math.pow(i, 2))
    for j in range(len(l) - 1):
        for k in range(len(l) - j - 1):
            if l[k] > l[k + 1]:
                l[k], l[k + 1] = l[k + 1], l[k]

print(l)
