from random import choice


class RandomWalk():
    """生成一个随机漫步数据的类"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            """使用 choice([1,-1]) 给 x_direction 选择一个值，结果要么是表示向右走的1，要么是表示向左走的-1"""
            x_direction = choice([1, -1])
            """ 
            choice([0,1,2,3,4]) 随机地选择一个0~4之间的整数，沿指定的方向走多远（ x_distance ）
            （通过包含0，我们不仅能够沿两个轴移动，还能够沿 y 轴移动。）
            """
            x_distance = choice([0, 1, 2, 3, 4])
            """如果 x_step 为正，将向右移动，为负将向左移动，而为零将垂直移动"""
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            """如果 y_step 为正，就意味着向上移动，为负意味着向下移动，而为零意味着水平移动"""
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            """如果 x_step 和 y_step 都为零，则意味着原地踏步，我们拒绝这样的情况，接着执行下一次循环"""
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的 x 和 y 值
            """为获取漫步中下一个点的 x 值，我们将 x_step 与 x_values 中的最后一个值相加"""
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            """获得下一个点的 x 值和 y 值后，我们将它们分别附加到列表 x_values 和 y_values的末尾"""
            self.x_values.append(next_x)
            self.y_values.append(next_y)



