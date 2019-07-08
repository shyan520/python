# 9--9.5 Python 标准库####################################################################
"""原始字典"""
favorite_languages = {}
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

print(favorite_languages)
for name,language in favorite_languages.items():
    print(name.title() + '会' + language.title())
print('\t')

"""模块`collections`中的`OrderedDict`类的实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序。"""
from collections import OrderedDict
"""调用`OrderedDict()`来创建一个空的有序字典"""
favorite_languages1 = OrderedDict()
favorite_languages1['jen'] = 'python'
favorite_languages1['sarah'] = 'c'
favorite_languages1['edward'] = 'ruby'
favorite_languages1['phil'] = 'python'

print(favorite_languages1)
for name,language in favorite_languages1.items():
    print(name.title() + '会' + language.title())
print('\t')

"""
模块`collections`中的`OrderedDict`类和dict普通字典的区别
使用dict时，key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果想要保持key的顺序，可以使用OrderedDict。OrderedDict的key会按照插入的顺序排列，不是key本身排序。
"""
li = {}
li['a'] = 'A'
li['b'] = 'B'
li['c'] = 'C'
la = {}
la['c'] = 'C'
la['b'] = 'B'
la['a'] = 'A'
print(li == la)

li = OrderedDict()
li['a'] = 'A'
li['b'] = 'B'
li['c'] = 'C'
la = OrderedDict()
la['c'] = 'C'
la['b'] = 'B'
la['a'] = 'A'
print(li == la)