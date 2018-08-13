# 作者 ljc
f = open("yesterday", "r", encoding="utf-8")
f_new = open("yesterday3", "w", encoding="utf_8")
for line in f:
    if "肆意的快乐" in line:
        line = line.replace("肆意的快乐", "一点都不快乐")
    f_new.write(line)
f.close()
f_new.close()