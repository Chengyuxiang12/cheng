list1 = [32, 3, 45, 2, 57, 13]
for i in range(len(list1)-1):
    for j in range(len(list1)-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print(list1)
