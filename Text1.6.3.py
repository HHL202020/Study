# P16 编程题
# 3.打印九九乘法表。
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%-2d "%(j,i,i*j),end='')       #%-2d后面的空格必须有
    print('')