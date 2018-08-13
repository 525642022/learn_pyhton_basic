# 作者 ljc
import shutil
# f=open("笔记",encoding="utf-8")
# f1=open("hhhjh","w")
#
# shutil.copyfileobj(f,f1)
shutil.copyfile("笔记","笔记1")
# shutil.copymode()仅拷贝权限 其他的都不变 内容组用户都不变
# shutil.copystat()拷贝状态信息
shutil.copystat("笔记","笔记1")
# shutil.copytree() 拷贝一个包里面所有的东西
# shutil.rmtree() 删除目录
# shutil.make_archive() 创建压缩包并返回文件路径

