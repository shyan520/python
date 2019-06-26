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
print('10--10.3.5\n ')

# 10--10.3.6 分析文本##########################################################################################
filename = r'test\Alice in Wonderland.txt'
try:
    with open(filename, 'r', encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print('该文件不存在')
# 当try代码块成功执行时，才执行else块中的代码
else:
    """方法`split()`以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中"""
    words = contents.split()
    print(len(words))
print('10--10.3.6\n ')

# 10--10.3.7 使用多个文件#######################################################################################
def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print('该文件不存在')
    else:
        words = contents.split()
        print('该文章中公有' + str(len(words)) + '个单词')

filenames = [r'test\Alice in Wonderland.txt1', r'test\Alice in Wonderland.txt']
for filename in filenames:
    count_words(filename)
print('10--10.3.7\n ')

# 10--10.3.8 失败时一声不吭#######################################################################################
filenames = [r'test\Alice in Wonderland.txt1', r'test\Alice in Wonderland.txt']
def test_count_words(filename):
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        """Python有一个`pass`语句，可在代码块中使用它来让 Python 什么都不要做"""
        pass
    else:
        print('该文章中公有' + str(len(contents.split())) + '个单词')
for filename in filenames:
    test_count_words(filename)
print('10--10.3.8\n ')