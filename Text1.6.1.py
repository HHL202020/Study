# P15 编程题
# 1.整数求和。输入整数n，计算1 ~ n之和。
n = int(input("请输入一个整数："))
sum = 0
for i in range(n+1):
    sum += i
print("1~%d的求和结果为%d"%(n,sum))
