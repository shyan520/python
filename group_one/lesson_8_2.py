# 8--8.6.1 导入整个模块###############################################################
from group_one import lesson_8_1, lesson_8_1 as le

# 调用lesson_8_1模块中的class_info()函数
print(lesson_8_1.class_info('三年级', '五班', people_number=48, teacher='李老师'))
print('8--8.6.1\n')

# 8--8.6.2 导入特定的函数#############################################################
from group_one.lesson_8_1 import class_info
print(class_info('三年级', '五班', people_number=48, teacher='李老师'))
print('8--8.6.2\n')

# 8--8.6.3 使用as给函数指定别名########################################################
# 把class_info()函数重命名为ci
from group_one.lesson_8_1 import class_info as ci
print(ci('三年级', '五班', people_number=48, teacher='李老师'))
print('8--8.6.3\n')

# 8--8.6.4 使用as给模块指定别名########################################################
# 把lesson_8_1模块重命名为le
# 调用lesson_8_1模块中的class_info()函数
print(le.class_info('三年级', '五班', people_number=48, teacher='李老师'))
print('8--8.6.4\n')

# 8--8.6.5 导入模块中的所有函数########################################################
from group_one.lesson_8_1 import *
print(class_info('三年级', '五班', people_number=48, teacher='李老师'))
print('8--8.6.5\n')

# 8.7 函数编写指南
# 应给函数指定描述性名称，且只在其中使用小写字母和下划线。
