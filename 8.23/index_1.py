# 定义一个列表
list1 = ['零','一','二','三','四','五','六','七','八','九']

for i in range(1,10):
    for j in range(1, i+1):
        # 乘积为个位数时
        if(len(str(i* j))==1):
            print('%s*%s=%s' % (list1[i], list1[j], list1[i * j]), end=' ')
        # 乘积为两位数时
        else:
            res = i * j
            num1 = res // 10
            num2 = res % 10
            print('%s*%s=%s%s' % (list1[i], list1[j], list1[num1], list1[num2]), end=' ')
    print()
