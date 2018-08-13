# 作者 ljc
# 获取相对路径
import os
import sys
print(__file__)
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import main

main.welcome()
