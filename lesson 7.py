# 7--7.1 函数 input() 的工作原理##################################################################
message = '欢迎光临！'
message += "\n请输入你的姓名："
name = input(message)
print('Hello ' + name)
print('7--7.1\n')

# 7--7.1.2 使用 int() 来获取数值输入################################################################
message = '欢迎光临！'
message += '\n请输入你的年龄：'
age = input(message)
if int(age) < 18:
    print('对不起，你未满十八岁，无法乘坐过山车')
else:
    print('请往前走，乘坐过山车')
print('7--7.1.2\n')

# 7--7.1.3 求模运算符################################################################################
print('4除3的余数 = ' + str(4 % 3))
print('5除3的余数 = ' + str(5 % 3))
print('6除3的余数 = ' + str(6 % 3))
print('7除3的余数 = ' + str(7 % 3))

# 计算你输入的数值是奇数还是偶数
number = input('请输入数字：')
if int(number) % 2 == 0:
    print('您输入的数字'+ str(number) +'是偶数')
else:
    print('您输入的数字'+ str(number) +'是奇数')
print('7--7.1.3\n')

# 7--7.2.1 使用while循环#############################################################################
number = 1
while number <= 5:
    print(number)
    number += 1
print('7--7.2.1\n')

# 7--7.2.2 让用户选择何时退出#########################################################################
prompt = '欢迎光临！请输入您的姓名：'
message = ''
while message != 'quit':
    message = input(prompt)
    print('注意：当输入quit时可以退出循环')
    print('你好！ ' + message)
print('7--7.2.2\n')

# 7--7.2.3 使用标志###################################################################################
prompt = '欢迎光临！请输入您的姓名：'
message = ''
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print('注意：当输入quit时可以退出循环')
        print('你好！ ' + message)
print('7--7.2.3\n')

# 7--7.2.4 使用break退出循环###################################################################################
prompt = '欢迎光临！请输入您的姓名：'
message = ''
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print('注意：当输入quit时可以退出循环')
        print('你好！ ' + message)
print('7--7.2.4\n')

# 7--7.2.5 在循环中使用continue###################################################################################
# 只打印奇数
# 方法一：
number =  range(1,11)
for value in number:
    if value % 2 == 0:
        continue
    print(value)
# 方法二：
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)
print('7--7.2.5\n')

# 7--7.3 使用while循环来处理列表和字典##############################################################################
# for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素
# 解释：由于在遍历的过程中，删除了其中一个元素，导致后面的元素整体前移，导致有个元素成了漏网之鱼。
#       同样的，在遍历过程中，使用插入操作，也会导致类似的错误。这也就是问题里说的无法“跟踪”元素。
# 例子1：
'''
numbers = [1,2,2,4,5,6]
for i,number in enumerate(numbers):
    if number == 2:
        del numbers[i]
    print(number)
'''
# 得到的是：1,2,4,5,6
# 例子2：
'''
numbers = [1,2,2,4,5,6]
for i in range(len(numbers)):
    if numbers[i] == 2:
        del numbers[i]
    print(numbers[i])
'''
# 得到的是：IndexError: list index out of range

# 正确的例子1：
numbers = [1,2,2,4,5,6]
i = 0
while i < len(numbers):
    if numbers[i] == 2:
        del numbers[i]
    else:
        print(numbers[i])
    i += 1

#正确的例子2：
numbers = [1,2,2,4,5,6]
print(numbers)
while 2 in numbers:
    numbers.remove(2)
print(numbers)
print('7--7.3\n')

# 7--7.3.3 使用用户输入来填充字典##############################################################################
responses = {}
bo = True
while bo:
    name = input('请问您的姓名：')
    response = input('您的回答是：')
    responses[name] = response
    reqeat = input('请问是否还需要询问别的客户？Y/N')
    if reqeat.upper() == 'N':
        bo = False
for k,v in responses.items():
    print(k + '的回答是：' + v)
print('7--7.3.3\n')