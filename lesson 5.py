# 5--5.1 一个简单if语句示例#################################################################
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print('5--5.1\n')

# 5--5.2.1 检查是否相等#####################################################################
car = 'bmw'
print(car == 'bmw')
print(car == 'audi')
print('5--5.2.1\n')

# 5--5.2.2 检查是否相等时不考虑大小写########################################################
car = 'Bmw'
print(car == 'bmw')
# 只有把car中的'Bmw'改成全部小写，再比较才会变成True
print(car.lower() == 'bmw')
# 函数lower()不会修改存储在变量car中的值
print(car)
print('5--5.2.2\n')

# 5--5.2.3 检查是否不相等#####################################################################
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('这不是小银鱼')
print('5--5.2.3\n')

# 5--5.2.4 比较数字###########################################################################
age = 18
print(age == 18)
if age != 20:
    print('他今年不是20岁')
print('5--5.2.4\n')

# 5--5.2.5 检查多个条件#######################################################################
age1 = 18
age2 = 20
# 全为True，则为True；反之，只要有一个为False，则为False
print(age1 <= 20 and age2 <= 20)
print(age1 < 18 and age2 == 20)
# 只要有一个为True，则为True
print(age1 < 18 or age2 == 20)
print('5--5.2.5\n')

# 5--5.2.6 检查特定值是否包含在列表中##########################################################
fruits = ['apple','banana','orange']
if 'apple' in fruits:
    print('苹果是水果')
if ('tree' in fruits) != True:
    print('树木不是水果')
print('5--5.2.6\n')

# 5--5.2.7 检查特定值是否不包含在列表中########################################################
fruits = ['apple','banana','orange']
if 'tree' not in fruits:
    print('树木不是水果')
print('5--5.2.7\n')

# 5--5.2.8 布尔表达式##########################################################################
# 布尔表达式的语义在于指明计算一个逻辑值的规则；从最基本的层次来说，所有的布尔表达式，不论它的长短如何，其值只能是true或false。
# 布尔表达式在程序设计语言中有两个基本的作用：
#   一是在某些控制语句中作为实现控制转移的条件；
#   另一个则是用于计算逻辑值本身。
game_active = True
can_edit = False
if game_active == can_edit:
    print('True')
else:
    print('False')
print('5--5.2.8\n')

# 5--5.3.3 if-elif-else结构#####################################################################
age = 19
if int(age) == 18:
    print('他今年满18岁了')
elif int(age) > 18:
    print('他今年大于18岁')
else:
    print('他今年未成年')
print('5--5.3.3\n')

# 5--5.3.5 省略 else 代码块######################################################################
age = 12
if int(age) == 18:
    print('他今年满18岁了')
elif int(age) > 18:
    print('他今年大于18岁')
elif int(age) < 18:
    print('他今年未成年')
print('5--5.3.5\n')

# 5--5.4 使用 if 语句处理列表#####################################################################
# 5--5.4.1 检查特殊元素###########################################################################
# 制作披萨的过程
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("加" + requested_topping + ".")
print("你的披萨做好了!!\n")
# 然而，如果比萨店的青椒用完了，该如何处理呢？
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('对不起，胡椒卖完了！')
    else:
        print("加" + requested_topping + ".")
print("你的披萨做好了!!")
print('5--5.4\n')

#5--5.4.2 确定列表不是空的#########################################################################
requested_toppings = []
if requested_toppings:
    print('此列表不为空')
else:
    print('此列表为空')
print('5--5.4.2\n')