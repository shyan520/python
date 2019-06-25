# 10--10.3 异常################################################################################################
# 10--10.3.1 处理ZeroDivisionError异常#########################################################################
# 10--10.3.2 使用 try-except 代码块############################################################################
try:
    print(5/0)
except ZeroDivisionError:
    print('不能除以0！')
print('10--10.3.2\n ')

# 10--10.3.5 处理FileNotFoundError异常#########################################################################
filename = r'test\pi_digits.txt'
filename1 = r'pi_digits.txt'
try:
    with open(filename1, 'r') as file_object:
        contents = file_object.read()
    print(contents)
except FileNotFoundError:
    print('该文件不存在')