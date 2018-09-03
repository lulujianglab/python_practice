import os
import filecmp
import shutil

path = "./files_0827"
dirs = ["file1", "file2", "file3", "file4"]

# 获取子文件夹中的文件列表
def get_all_files(path, dirs):
    all_files = []
    for dir in dirs:
        current_path = path + "/" + dir
        files = os.listdir(path + "/" + dir)
        for file in files:
            all_files.append(current_path + "/" + file)

    return all_files

# 获取"./files_0827"中的文件
def get_all_files2(path, dirs):
    all_files = []
    files = os.listdir(path)
    for file in files:
        if "." in file:
            all_files.append(path + "/" + file)

    return all_files

# 对比all_files中各个文件的内容是否相同，相同则删除
def compare_file(x, y):
    if filecmp.cmp(x, y):
      os.remove(y)

# 实现文件去重
all_files = get_all_files(path, dirs) + get_all_files2(path, dirs)

for file1 in all_files:
    for file2 in all_files:
        if file1 != file2 and os.path.exists(file1) and os.path.exists(file2):
            compare_file(file1, file2)

print("去重操作完成。")

# 文件归类
all_files = get_all_files(path, dirs) + get_all_files2(path, dirs)
for file in all_files:
    file_type = file.split(".")[-1]
    if not os.path.exists(path + "/" + file_type):
        os.makedirs(path + "/" + file_type)
        shutil.move(file,path + "/" + file_type)
    else:
        shutil.move(file, path + "/" + file_type)

print("文件归类完成")

# 删除空文件夹
for dir in dirs:
    os.removedirs(path + "/" +dir)

all_type = os.listdir(path)
for type in all_type:
    zip_name = path + "/" + type
    shutil.make_archive(zip_name, "zip", zip_name)
    shutil.rmtree(zip_name)  # 递归删除文件夹

print("文件打包完成。")