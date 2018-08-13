import getpass

# 用户注释1
name = "Thank Liu"
name2 = name
"""用户注释2
用户注释3
"""
print("My name is", name, name2)

name = "PaoChe Ge"

print(name, name2)
username = input("username:")
password = input("passWord:")

_username = "ljc"
_password = "sss"
age = input("age:")
job = input("job:")
print(type(job), type(age))
info = f'''
name {username} 
age {age}
job {job}
'''
print(info)
if _username == username and _password == password:
    print("success", username, password)
else:
    print("default", _username, _password)
