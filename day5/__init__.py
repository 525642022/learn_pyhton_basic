# 作者 ljc
#1 定义
# 模块：聪明逻辑上组织py代码（函数 变量 逻辑 本质：实现一个功能）本质就是一个一py为结尾的python文件
# 包： 本质就是一个目录（必须带__init__.py）
# 2导入方法
# import module_name
# import module_name, module_name2
# from module_name import *（不建议使用这种方法）
# from与import区别 from表示把所有的代码复制到当前模块中
# from module_name import test as
# 别名 给导入的方法起一个别名防止重复
# 3 import本质
# 把模块运行一遍 把结果给新模块付给一个你导入的变量
# from只把模块中的某一部分导入新模块 没有新赋值
# import module_name--> module_name.py--->路径-->sys.path
# 导入包的本质就是解释包下面的init文件
# 导入优化
# 模块的分类
# 分为三大类
# a标准库
# 1. time与datatime
# b开源模块
# c自定义模块