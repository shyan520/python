# 9--9.1.1 创建Dog类#################################################################
# 首字母大写的名称指的是类
class Dog():
    """一次模拟小狗的简单尝试"""
# 方法__init__()是一个特殊的方法，每当你根据`Dog`类创建新实例时，Python 都会自动运行它。
# self代表类的实例，而非类
    def __init__(self, name, age):
        """初始化name和age的属性"""
        # 以self为前缀的变量表示本类中的所有方法都能使用带self前缀的变量，我们还可以通过类的任何实例来访问这些变量
        # self指的是类实例对象本身而不是类本身。个人认为self的作用主要是标示公有成员变量的作用。
        # 如果我在类的一个方法定义了一个变量，这个变量就唯一的属于这个方法，如果其他方法想用这个变量呢？不好意思，不能使用。
        # 而使用self则可以解决这个问题，self会告诉所有的方法：这个变量是我们共有的，可以随便用哟
        # 如果把self去掉，写成 name1 = name，那name1就只属于_init_方法，sit和roll_over方法都不能使用
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + '现在坐下！')

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + '现在打滚！')

# 9--9.1.2 根据类创建实例#############################################################
"""创建Dog类的实例，实例名称为my_dog"""
my_dog = Dog('小白', 6)
# 访问my_dog实例下属性name的值
print('我的小狗的名字叫：' + my_dog.name.title() + '。')
print('它的年龄是：' + str(my_dog.age) + '。')
"""让小狗蹲下"""
my_dog.sit()
"""让小狗打滚"""
my_dog.roll_over()
print('\n')

# 创建多个实例
"""在创建Dog类的第二个实例，实例名称为your_dog"""
your_dog = Dog('天天', 2)
print('她的小狗的名字叫：' + your_dog.name.title() + '。')
print('它的年龄是：' + str(your_dog.age) + '。')
your_dog.sit()
your_dog.roll_over()
print('9--9.1.2\n')
