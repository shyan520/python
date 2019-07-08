# 10--10.1.1 读取整个文件####################################################################


class FileReader():
    def __init__(self, filepath):
        self.filepath = filepath

    def file_reader(self):
        """
        关键字`with`在不再需要访问文件后将其关闭。在这个程序中，注意到我们调用了`open()`，但没有调用`close()`；
        你也可以调用`open()`和`close()`来打开和关闭文件，但这样做时，如果程序存在 bug，导致`close()`语句未执行，文件将不会关闭。
        """
        with open(self.filepath) as file_object:
            contents = file_object.read()
            print(contents)


"""另外一种绝对路径的写法为：D:/Python代码/python/test/pi_digits.txt"""
file_path = r'D:\Python代码\python\test\pi_digits.txt' #设置需要读取的文件路径--绝对路径
file_path1 = 'test/pi_digits.txt' #设置需要读取的文件路径--相对路径
fr = FileReader(file_path)
fr.file_reader()
fr = FileReader(file_path1)
fr.file_reader()
print('10--10.1.1\n ')

# 10--10.1.3 逐行读取####################################################################
with open(file_path1) as file_object:
    for line in file_object:
        print(line)
print('10--10.1.3\n ')

# 10--10.1.4 创建一个包含文件各行内容的列表##############################################
with open(file_path1) as file_object:
    """方法`readlines()`从文件中读取每一行，并将其存储在一个列表中"""
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())  # rstrip()消除多余的空白行
print('10--10.1.4\n ')

# 10--10.1.5 使用文件的内容##############################################################
with open(file_path1) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
print('10--10.1.5\n ')

# 10--10.1.6 包含一百万位的大型文件#######################################################
file_path2 = r'test\pi_string.txt'
with open(file_path2) as file_object:
    lines = file_object.readlines()

pi_line = ''
for line in lines:
    pi_line += line.strip()
"""显示圆周率钱52位数字"""
print(pi_line[:52] + '...')
"""查看你的生日是否在圆周率中"""
#birthday = input('请输入你的生日：')
birthday = '19821030'
if birthday in pi_line:
    print('你的生日在圆周率中')
else:
    print('非常抱歉，你的生日不在圆周率中')

# 查找&替换
"""把dog找出来，替换成cat"""
pi = "I really like dogs"
pi = pi.replace('dog', 'cat')
print(pi)
print('10--10.1.6\n ')

# 10--10.2.1 写入空文件####################################################################
filename = r'test\null_message.txt'
# encoding='utf-8'解决写入中文乱码的问题
with open(filename, 'w', encoding='utf-8') as file_object:
    file_object.write('我写入了第一行文字\t')
    file_object.write('我写入了第二行文字\n')
    file_object.write('我写入了第三行文字\n')
    file_object.write('我写入了第四行文字\n')

with open(filename, 'r', encoding='utf-8') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())
print('10--10.2.1\n ')

# 10--10.2.3 附加到文件####################################################################
with open(filename, 'a', encoding='utf-8') as file_object:
    file_object.write('我最追加了一行数据')

with open(filename, 'r', encoding='utf-8') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())
print('10--10.2.3\n ')