# 9--9.4 导入类##################################################################################
"""一个可用于表示汽车的类"""


class Car():
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回车子的描述信息"""
        long_name = '这辆车的牌子是：' + self.make + '；型号是：' + self.model + '；车龄为：' + str(self.year)
        return long_name.title()

    def get_odometer(self):
        """打印一条信息，来显示车子的行驶里程"""
        print('这辆车子的行驶里程为' + str(self.odometer_reading) + '公里。')

    def set_odometer(self, odometer):
        if odometer >= self.odometer_reading:
            self.odometer_reading = odometer
        else:
            print("您不能回滚里程数")

# 9--9.4.2 在一个模块中存储多个类#####################################################################


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('这辆汽车的电瓶容量为：' + str(self.battery_size) + '-kWh')

    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = '这辆车充一次电大约能跑' + str(range)
        message += '公里'
        print(message)


class ElectricCar(Car):
    """模拟电动车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类属性，再初始化电动车特有属性"""
        super().__init__(make, model, year)
        self.battery = Battery()