# 作者 ljc 使用with打开文件后会自动关闭
with open("yesterday", "r") as f:
    for line in f:
        print(line)
