import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # Bullet 类继承了我们从模块 pygame.sprite 中导入的 Sprite 类
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        # 使用了 Python 2.7 语法。这种语法也适用于 Python 3
        # 但也可以将这行代码简写为 super().__init__()
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        # 因为子弹并非基于图像的，所以使用 pygame.Rect() 类从空白开始创建一个矩形
        # 创建这个类的实例时，必须提供矩形左上角的 x 坐标和 y 坐标，还有矩形的宽度和高度。
        # 默认在屏幕左上角(0,0)处创建这个矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        """把子弹的初始位置移动到正确位置--飞船的头部位置"""
        # 将子弹的 centerx 设置为飞船的 rect.centerx
        self.rect.centerx = ship.rect.centerx
        # 子弹应从飞船顶部射出，因此我们将表示子弹的 rect 的 top 属性设置为飞船的 rect 的 top 属性，让子弹看起来像是从飞船中射出的
        self.rect.top = ship.rect.top

        """存储用小数表示的子弹位置"""
        # 将子弹的y坐标存储为小数值，以便能够微调子弹的速度
        self.y = float(ship.rect.y)

        """设置子弹的颜色"""
        self.color = ai_settings.bullet_color
        """设置子弹的速度"""
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """管理子弹的位置；向上移动子弹"""
        # 更新表示子弹位置的小数值
        # 发射出去后，子弹在屏幕中向上移动，这意味着 y 坐标将不断减小
        self.y -= self.speed_factor
        # 更新表示子弹的 rect 的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
