while True:
    a = input("请输入一个整数(输入q结束)：")
    if a == "q":
        break
    b = input("请输入一个整数(输入q结束)：")
    if b == "q":
        break
    try:
        a = int(a)
        b = int(b)
        print("两个数的和为：" + str(a + b))
    except ValueError:
        print("请输入整数！")
