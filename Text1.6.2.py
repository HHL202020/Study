# P16 编程题
# 2.整数排列。输入3个整数，把这3个数由小到大输出。
l=[]
for i in range(3):
    x = int(input('请输入整数：'))
    l.append(x)
l.sort()
print(l)