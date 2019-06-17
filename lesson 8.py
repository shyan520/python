# 8--8.1 定义函数##################################################################
def greet_user():
    print('Hello!')
greet_user()
print('8--8.1\n')

# 8--8.1.1 向函数传递信息###########################################################
# userName是形参；'yanshunhua'是实参
def greet_user(userName):
    print('Hello! ' + userName)
greet_user('yanshunhua'.title())
print('8--8.1.1\n')

# 8--8.2.1 位置实参#################################################################
def greet_user(userName,sex):
    print('Hello! ' + userName + sex)
greet_user('yanshunhua'.title(),'男士')
# 调用函数多次
greet_user('xuhongjia'.title(),'女士')
print('8--8.2.1\n')

# 8--8.2.2 关键字实参###############################################################
def greet_user(userName,sex):
    print('Hello! ' + userName + sex)
greet_user(userName='yanshunhua'.title(),sex='男士')
# 调用函数多次
greet_user(sex='女士',userName='xuhongjia'.title())
print('8--8.2.2\n')

# 8--8.2.3 默认值###################################################################
# 设置sex形参的默认值是'男士'
def greet_user(userName,sex = '男士'):
    print('Hello! ' + userName + sex)
# 输入实参的时候，特地缺损sex参数的输入
greet_user(userName='yanshunhua'.title())
# 调用函数多次
greet_user(sex='女士',userName='xuhongjia'.title())
print('8--8.2.3\n')

# 8--8.3.1 返回简单值###############################################################
def greet_user(firstName,lastName):
    userName = firstName + ' ' + lastName
    return userName.title()
name= greet_user('yan','shunhua')
print('Hello! ' + name)
print('8--8.3.1\n')

# 8--8.3.3 返回字典#################################################################
def greet_user(firstName,lastName,age = ''):
    user = {'first':firstName,'last':lastName}
    if age:
        user['age'] = age
    return user
print(greet_user('yan','shunhua',27))
print('8--8.3.3\n')

# 8--8.3.4 结合使用函数和while循环################################################
def greet_user(firstName,lastName):
    userName = firstName + ' ' + lastName
    return userName

bo = True
while bo:
    f_name = input('您好，请输入姓：')
    l_name = input('请输入名字：')
    print('早上好！ '+ greet_user(f_name,l_name).title())
    if input('是否还需要再登记？Y/N').upper() == 'N':
        bo = False

import copy
# 初始化users列表
users = []
# 初始化单个人信息字典
user = {}
sign = True
while sign:
# 方法一：
    user['name'] = input('请输入姓名：')
    user['age'] = input('请输入年龄：')
# 方法二：
#    name = input('请输入姓名：')
#    age = input('请输入年龄：')
# 深copy和浅copy的解释https://blog.csdn.net/w494675608/article/details/82114798
# 方法一：
    users.append(copy.deepcopy(user))
# 方法二：
#    user = {'name':name,'age':age}
#    users.append(user)
    if input("是否需要继续输入？Y/N").upper() == 'N':
        sign = False
for user in users:
    print(user)
print('8--8.3.4\n')
'''

# 8--8.4.1 在函数中修改列表#########################################################
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
#  打印每个设计后，都将其移到列表 completed_models 中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #模拟根据设计制作 3D 打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


