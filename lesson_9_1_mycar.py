# 9--9.4.1 导入单个类############################################################################
from lesson_9_1_car import Car

my_new_car = Car('audi','a4',1)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 100
my_new_car.get_odometer()

my_new_car.set_odometer(120)
my_new_car.get_odometer()
print('\t')

# 9.4.2 在一个模块中存储多个类===============导入同模块中的另外一个单类
from lesson_9_1_car import ElectricCar
my_electric_car = ElectricCar('tesla', 'model s', 1)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()

# 9--9.4.3 从一个模块中导入多个类#####################################################################
from lesson_9_1_car import Car,ElectricCar
my_car = Car('BMW', '3系列', 2)
print(my_car.get_descriptive_name())

my_electric_car = ElectricCar('荣威', '550', 3)
print(my_electric_car.get_descriptive_name())
print('\t')

# 9--9.4.4 导入整个模块#####################################################################
import lesson_9_1_car as car
my_car1 = car.Car('别克', '君越', 4)
print(my_car1.get_descriptive_name())
my_electric_car1 = car.ElectricCar('别克', '昂科威', 5)
print(my_electric_car1.get_descriptive_name())
print('\t')

# 9--9.4.5 导入模块中的所有类################################################################
"""不推荐使用这种方式来导入所有类，容易和别的同名的类产生冲突"""
from lesson_9_1_car import *
"""需要从一个模块中导入很多类时，最好导入整个模块，并使用*module_name.class_name*语法来访问类"""

# 9--9.4.6 在一个模块中导入另一个模块#########################################################
"""
把lesson_9_1_car模块中的Electric()类和Battery()类抽离出来，组合成一个名叫lesson_9_1_electric模块，
然后再分别实例化lesson_9_1_car模块中的Car()类和lesson_9_1_electric模块中的Electric()类，
一样可以使用继承关系
"""