# 作者 ljc
import sys,os
print(sys.path)
DIR_NAME=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,DIR_NAME)
print(DIR_NAME)
import main
main.test()
