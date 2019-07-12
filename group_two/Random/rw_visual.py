import matplotlib.pyplot as plt

from group_two.Random.random_walk import RandomWalk

sing = True
while sing:
    rw = RandomWalk()
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    """函数 figure() 用于指定图表的宽度、高度、分辨率和背景色"""
    plt.figure(figsize=(10, 6))

    """使用了 range() 生成了一个数字列表，其中包含的数字个数与漫步包含的点数相同。接下来，将这个列表存储在 point_numbers 中，以便后面使用它来设置每个漫步点的颜色"""
    point_numbers = list(range(rw.num_points))
    """ edgecolor=none 以删除每个点周围的轮廓；最终的随机漫步图从浅蓝色渐变为深蓝色"""
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=10)
    """标记起点位置"""
    plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolor='none', s=50)
    """标记终点位置"""
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=50)

    """隐藏X坐标轴"""
#    plt.axes().get_xaxis().set_visible(False)
    """隐藏y坐标轴"""
#    plt.axes().get_yaxis().set_visible(False)
    """隐藏X和Y坐标轴"""
    plt.axis('on')

    plt.show()

    if input("是否需要退出模拟？Y/N").lower() == 'y':
        sing = False
