import os

'''
author:jianglu
time: 2018/8/27
function : operate folder
'''

# 文件搜索函数
def file_serch(path):
    file_names = os.listdir(path)
    file_name = input("请输入文件全名或部分文件名：")
    for file in file_names:
        if file_name in file:
            print("文件位置为：%s/%s" % (path, file))

# 文件保存
def file_save(path):
    """
    根据输入目录得到目录下的文件名 文件类型 并保存到files.txt中
    :return:
    """
    file_names = os.listdir(path)

    file1 = open("files.txt", "a")
    for file_name in file_names:
        file_name_sp = file_name.split(".")
        file_name = file_name_sp[0]
        file_type = file_name_sp[1]
        file1.write(file_name.ljust(20))
        file1.write(file_type + "\n")
    file1.close()
    print("文件信息已保存")

#文件重命名
def file_remname(path):
    """
    根据查找到的用户名进行替换用户名操作
    :return:
    """
    file_names = os.listdir(path)

    file_fullname = input("请输入文件名：")
    file_name_new = input("请输入新文件名：")
    os.rename(path + "/" + file_fullname, path + "/" + file_name_new)
    print("文件已重命名")

def file_manager():
    """
    主函数
    """
    path = input("请输如文件路径(父子目录间用/分隔)：")
    flag = False
    while True:
        if flag:
            path = input("请输如文件路径(父子目录间用/分隔)：")
        if not os.path.exists(path) or "." in path:
            print("输入路径有误，请重新输入：")
            flag = True
            continue
        print("文件管理系统：")
        print("文件搜索：  1")
        print("文件保存：  2")
        print("文件重命名： 3")
        print("退出请输入q")
        op = input("请选择您的操作：")

        if op == "1":
            file_serch(path)
        elif op == "2":
            file_save(path)
        elif op == "3":
            file_remname(path)
        else:
            break

        answer = input("是否继续操作当前文件夹？(y/n)")
        if answer == "y":
            flag = False
            continue
        else:
            flag2 = input("是否切换路径？(y/n)")
            if flag2 == "y":
                flag = True
                continue
            else:
                break


file_manager()



