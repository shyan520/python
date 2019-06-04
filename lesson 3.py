# 3--3.1 列表是什么#################################################################
stringList = ['trek','cannondale','redline','specizlized']
print(stringList)
print('3--3.1\n')

# 3--3.1.1 访问列表元素#############################################################
stringList = ['trek','cannondale','redline','specizlized']
print(stringList[0])
print(stringList[-2])
print('3--3.1.1\n')

# 3--3.2.1 修改列表元素#############################################################
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
print('3--3.2.1\n')

# 3--3.2.2 在列表中添加/插入元素####################################################
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(1,'ducati')
print(motorcycles)
print('3--3.2.2\n')

# 3--3.2.3 在列表中删除元素#########################################################
#方法1：del
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#方法2：pop()
# 方法 pop() 可删除列表末尾的元素，并让你能够接着使用它。术语 弹出 （ pop ）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
# 如果你不确定该使用 del 语句还是 pop() 方法，下面是一个简单的判断标准：如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用 del 语句；
#                                                                       如果你要在删除元素后还能继续使用它，就使用方法 pop() 。
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles.pop(0))

#方法3：pop()
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)
print('3--3.2.3\n')

# 3--3.3.1 使用方法 sort() 对列表进行永久性排序########################################
cars = ['bmw','audi','toyota','subaru']
# 按字母顺序排序
cars.sort()
print(cars)
# 按字母反向顺序排序
cars.sort(reverse=True)
print(cars)
print('3--3.3.1\n')

# 3--3.3.2 使用函数 sorted() 对列表进行临时排序#########################################
cars = ['bmw','audi','toyota','subaru']
print(cars)
print(sorted(cars))
print(sorted(cars,reverse=True))
print(cars)
print('3--3.3.2\n')

# 3--3.3.3 反转列表元素的排列顺序进行排序###############################################
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
print('3--3.3.3\n')

# 3--3.3.4 确定列表长度#################################################################
# Python计算列表元素数时从 1 开始，因此确定列表长度时，不会遇到差一错误。
cars = ['bmw','audi','toyota','subaru']
print(len(cars))
print('3--3.3.4\n')



