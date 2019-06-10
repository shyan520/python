# 4--4.1 遍历整个列表#################################################################
listName = ['alice','david','ella']
for li in listName:
    print(li)
print('4--4.1\n')

# 4--4.1.2 在 for 循环中执行更多的操作################################################
listName = ['alice','david','ella']
for li in listName:
    print(li.title() + '，表扬太精彩了')
    print('期待他的下次表演')
print('4--4.1.2\n')

# 4--4.3 创建数值列表##################################################################
for value in range(1,5):
    print(value)
print('4--4.3\n')

# 4--4.3.2 使用 range() 创建数字列表###################################################
numbers = list(range(1,6))
print(numbers)
# 使用函数 range() 时，还可指定步长。例如，下面的代码打印 1~10 内的偶数
numbers = list(range(2,11,2))
print(numbers)
# 代码打印 1~10 内的奇数
numbers = list(range(1,11,2))
print(numbers)
# 代码打印 1~10 的平方
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)
print('4--4.3.2\n')

# 4--4.3.3 对数字列表执行简单的统计计算################################################
# 求数值中的最小值
print(min(squares))
# 求数值中的最大值
print(max(squares))
# 求数值的总和
print(sum(squares))
print('4--4.3.3\n')

# 4--4.3.4 列表解析#####################################################################
# 将 for 循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value**2 for value in range(1,11)]
print(squares)
print('4--4.3.4\n')

# 4--4.4 使用列表的一部分###############################################################
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print('4--4.4\n')

# 4--4.4.1 切片#########################################################################
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 获取列表中的第2个到第4个
print(players[1:4])
# 获取列表中的前2个
print(players[:2])
# 获取列表中的后2个
print(players[3:])
print(players[-2:])
print('4--4.4.1\n')