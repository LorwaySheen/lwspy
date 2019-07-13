a = input("请输入一个整数：")
b = input("请输入一个整数：")
try:
    a = int(a)
    b = int(b)
    print("两个数的和为：" + str(a + b))
except ValueError:
    print("请输入整数！")