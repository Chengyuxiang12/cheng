list1 = [32, 3, 45, 2, 57, 13]  # 定义数组
for i in range(len(list1) - 1):  # 排序次数
    for j in range(len(list1) - i - 1):  # 对比次数
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]  # 比较这次数值与下一数值大小，如果大于下一数值则调换位置

print(list1)  # 输出数组
