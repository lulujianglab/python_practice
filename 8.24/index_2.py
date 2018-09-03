# 导入os模块
import os

# 查找函数

def find():
    path = input("输入您要查找文件目录:")
    name = input("输入您要查找的文件名:")
    type = input("输入您要查找的文件类型:")

    files = os.listdir(path)
    for f in files:
        if f.endswith(type) and name in f:
            print(f)

# 文件保存

def save():
    path2 = input("输入您要查找文件目录:")
    files2 = os.listdir(path2)
    file1 = open("files.txt", "a")
    for f2 in files2:
        file_type = os.path.splitext(f2)[1]
        file_name = os.path.splitext(f2)[0] # 去掉文件名
        file1.write(file_name.ljust(20))
        file1.write(file_type + "\n")
    file1.close()

# 文件重命名

def remname():
    path = input("输入您要查找文件目录:")
    file_fullname = input("请输入文件名：")
    file_name_new = input("请输入新文件名：")
    os.rename(path + "/" + file_fullname, path + "/" + file_name_new)
    print("文件已重命名")

def file_manager():
    while True:
        print("文件管理系统:")
        print("1、文件搜索:")
        print("2、文件保存:")
        print("3、文件重命名:")
        op = input("请选择您的操作:")

        if op == "1":
            find()
        elif op == "2":
            save()
        elif op == "3":
            remname()
        else:
            break

file_manager()