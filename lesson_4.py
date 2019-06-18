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
print('\n')

# 进阶例子
import copy
li = [1,2,3,4,[1,2,3]]
new_li = li
copy_li = copy.copy(li)
deepcopy_li = copy.deepcopy(li)

print(id(li))
print(id(new_li))
print(id(copy_li))
print(id(deepcopy_li))
print('可以看到，使用copy这个模块创建的浅拷贝和深拷贝在内存中都有一个新的内存空间。\n')
print(id(li[1]))
print(id(new_li[1]))
print(id(copy_li[1]))
print(id(deepcopy_li[1]))
print('\n')
print(id(li[-1]))
print(id(new_li[-1]))
print(id(copy_li[-1]))
print(id(deepcopy_li[-1]))
print('浅拷贝是不会对li中的数据结构进行深层次的拷贝的。'
      '也就是说，我要是在li列表，更改了li[-1]的值，那么copy_li中的最后一个元素的值是会跟着改变的，'
      '因为他跟li引用的地址是同一个，而deepcopy_li的值是不会变的。\n')
print(li)
print(li[::-1])
print('list[indexStart: indexEnd: step]，当step>0的时候，正向取值，也就是从左往右取值，'
      '当step<0时，逆向取值。所以li[::-1]都是取的列表的逆序表，也就是从右往左取值。')
print('li[:4] = li[:-1] --- ' + str(li[:4]) + ' = ' + str(li[:-1]))
print('分片操作其实就是按照一定的顺序访问序列中某一范围内的元素，记住一点就行了，那就是在一定的访问顺序中，'
      'indexStart所对应的元素必须先于indexEnd所对应的元素被访问到，否则，分片操作返回的就是空的序列；'
      '而访问元素的顺序由step决定是从左往右，还是从右往左。')
print('4--4.4.1\n')

# 4--4.4.3 复制列表#####################################################################
my_foods = ['pizza', 'falafel', 'carrot cake']
# 正确的复制列表方法： 把my_foods整个列表的切片值赋值给新的friend_foods列表
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('正确的：' + str(my_foods))
print('正确的：' + str(friend_foods))
print('\n')

my_foods = ['pizza', 'falafel', 'carrot cake']
# 错误的复制列表方法： 将新变量 friend_foods 关联到包含在my_foods中的列表，因此这两个变量都指向同一个列表
friend_foods = my_foods
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('错误的：' + str(my_foods))
print('错误的：' + str(friend_foods))
print('4--4.4.3\n')

# 4--4.5 元组#########################################################################
# Python没有数组：
# 只有元组(tuple)和列表(list)；
# 元组一旦创建不可改变，例如：aa=tuple(1,2,3)；
# 元组不能追加(append)元素，弹出(pop)元素等；
# 只能对元组中的元素进行索引aa[0]，不能对其中的元组进行赋值aa[0]=8；
# 使用元组的好处在于对元组进行操作更为高效，适合存放一组常量；
# 而上述的众多不可以，使用列表list是可以的。
# 4--4.5.1 定义元组###################################################################
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# 尝试修改第一个元素的值
# dimensions[0] = 250
#报错日志：TypeError: 'tuple' object does not support item assignment
print('4--4.5.1\n')

# 4--4.5.2 遍历元组中的所有值#########################################################
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
print('4--4.5.2\n')

# 4--4.5.3 修改元组变量###############################################################
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值
dimensions = (250,100,50)
for dimension in dimensions:
    print(dimension)
print('4--4.5.3\n')

# 4--4.6 代码格式#####################################################################
# 可以参考PEP 8 -- Style Guide for Python Code编码格式
# 访问地址：https://www.python.org/dev/peps/pep-0008