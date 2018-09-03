# 定义函数

# 相加
def add(x, y):
    return x + y

# 相减
def subtract(x, y):
    return x - y

# 相乘
def multiply(x, y):
    return x * y

# 相除
def divide(x, y):
    return x / y

# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

num = input("输入你的选择(1/2/3/4):")

num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

if num == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif num == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif num == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif num == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("非法输入")
