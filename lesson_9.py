# 9--9.1.1 创建Dog类#################################################################
# python3编程中的if __name__ == '__main__': 的作用和原理:https://www.jianshu.com/p/c316646e42bc
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

# 9--9.2 使用类和实例#################################################################
class Car():
    """给属性year定义默认值"""
    def __init__(self, make, model, year=10, ):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 初始化初始公里数为0
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = self.make + ' ' + self.model + ' ' + str(self.year)
        return  long_name

    def set_read_odometer(self, mdometer):
        # 更新公里数为制定的数值
        self.odometer_reading = mdometer

    def get_read_odometer(self):
        print('车辆行驶了' + str(self.odometer_reading) + '公里')

my_car = Car('audi', 'a4', 8)
print(my_car.get_descriptive_name())
print('9--9.2\n')

# 9--9.2.3 修改属性的值###############################################################
# 对Car类中的make属性重新进行赋值
my_car.make = 'BMW'
print(my_car.get_descriptive_name())

# 通过方法修改odometer_reading属性
my_car.set_read_odometer(23)
my_car.get_read_odometer()
print('9--9.2.3\n')

# 9--9.3 继承#########################################################################
class Motor():
    def __init__(self, make, model, year,):
        self.make = make
        self.model = model
        self.year = year
        # 行驶公里默认为0公里
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = '这辆摩托车的牌子是：' + self.make + '； 型号是：'+ self.model + '； 车龄是：' + str(self.year) + '年'
        return long_name

    def get_read_odometer(self):
        print('目前行驶公里数为：' + str(self.odometer_reading) + '公里')

    def set_read_odometer(self, odometer):
        if odometer >= self.odometer_reading:
            self.odometer_reading = odometer
        else:
            print("您不能回滚里程数")

    def fill_gas_tank(self):
        print('这辆车每次使用需要加满油箱')

class ElectricMotor(Motor):
    """电动摩托车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        # 9--9.3.1 子类的方法__init__()
        # super()`是一个特殊函数，帮助 Python 将父类和子类关联起来。
        # 这行代码让 Python 调用`ElectricMotor`的父类的方法`__init__()`，让`ElectricMotor`实例包含父类的所有属性。
        # 父类也称为**超类**（superclass），名称 super 因此而得名。
        super().__init__(make, model, year)
        # 9--9.3.3 给子类定义属性和方法=======初始化电动摩特车特有的属性'battery_size'
        self.battery_size = 70000

    # 9--9.3.3 给子类定义属性和方法=======电动摩托车特有的方法
    def describe_battery(self):
        print('这辆电动摩托车的电瓶容量是' + str(self.battery_size) + '安培')

    # 9--9.3.4 重写父类的方法===========重写父类fill_gas_tank方法
    def fill_gas_tank(self):
        print('电动摩托车不需要加油')

my_motor = Motor('哈雷', '800', 5)
print(my_motor.get_descriptive_name())
my_motor.fill_gas_tank()
print('\n')
my_electricmotor = ElectricMotor('雅马哈', 'T400', 1)
print(my_electricmotor.get_descriptive_name())
my_electricmotor.describe_battery()
my_electricmotor.fill_gas_tank()
print('\n')

# 9--9.3.5 将实例用作属性######################################################################
# 定义了一个名为`Battery`的新类，它没有继承任何类
class Battery():
    """第一次模拟电动摩托车电瓶的简单尝试"""
    def __init__(self, battery_size=7000):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('这辆电动摩托车的电瓶容量是' + str(self.battery_size) + '安培')

class ElectricMotor1(Motor):
    """电动车的独特之处"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #  创建一个新的`Battery`实例（由于没有指定尺寸，因此为默认值`70`），并将该实例存储在属性`self.battery`中。
        #  每当方法`__init__()`被调用时，都将执行该操作；因此现在每个`ElectricMotor`实例都包含一个自动创建的`Battery`实例。
        self.battery = Battery()

my_electricmotor = ElectricMotor1('太子', 'S1000', 0)
print(my_electricmotor.get_descriptive_name())
my_electricmotor.battery.describe_battery()
# 对Battery()类中的battery_size属性进行重新赋值
my_electricmotor.battery.battery_size = 10000
my_electricmotor.battery.describe_battery()




