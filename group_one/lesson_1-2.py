# 1--1.1.3 Hello Word程序#######################################
print('Hello Word!')
print('1--1.1.3\n')

# 2--2.2.1 变量的命名和使用#####################################
# 定义变量message
message = 'Hello Word!'
print(message)
message = 'Hello Python Crash Course Word!'
print(message)
print('2--2.2.1\n')

# 2--2.3.1 使用方法修改字符串的大小写############################
name = "ada loveLACE"
print(name)
# title()把字符串中的单词首字母自动转换成大写,其他的小写
print(name.title())
# upper()把字符串中的字母全部大写
print(name.upper())
# lower()把字符串中的字母全部小写
print(name.lower())
print('2--2.3.1\n')

# 2--2.3.2 合并（拼接）字符串#####################################
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " +last_name
print(first_name+last_name)
print(full_name)
print("Hello, " + full_name.title() + "!")
print('2--2.3.2\n')

# 2--2.3.3 使用制表符或换行符来添加空白###########################
print("Python test")
print("Python\ttest")
print("Python\ntest")
print('2--2.3.3\n')

# 2--2.3.4 删除字符串首尾的空格################################################
favorite_language = ' python '
print(favorite_language)
# rstrip()删除字符串末尾的空格
favorite_language = favorite_language.rstrip()
print(favorite_language)
# lstrip()删除字符串首端的空格
favorite_language = favorite_language.lstrip()
print(favorite_language)
print('2--2.3.4\n')

# 2--2.4.1 整数#################################################################
count = 2 + 3
print(count)
count = 2 - 3
print(count)
count = 2 * 3
print(count)
count = 2 / 3
print(count)
#  使用两个乘号表示乘方运算
count = 2 ** 3
print(count)
count = 3 ** 3
print(count)
# 支持运算次序
count = 2 + 3 * 4
print(count)
count = (2 + 3) * 4
print(count)
print('2--2.4.1\n')

# 2--2.4.2 浮点数#################################################################
count = 0.1 + 0.1
print(count)
count = 0.2 - 0.3
print(count)
count = 2 * 0.3
print(count)
count = 2 / 0.3
print(count)
print('2--2.4.2\n')

# 2--2.4.3 使用函数str()避免类型错误###############################################
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)