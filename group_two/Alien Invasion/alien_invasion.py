import pygame
from pygame.sprite import Group

from group_two.settings import Settings
from group_two.ship import Ship
import group_two.game_functions as gf

"""主文件；要玩游戏《外星人入侵》，只需运行文件 alien_invasion.py"""


def run_game():
    """初始化游戏，并创建一个屏幕对象"""
    pygame.init()
    """创建一个名为screen的显示窗口"""
    # 对象screen是一个surface。在Pygame中，surface是屏幕的一部分，用于显示游戏元素。在这个游戏中，每个元素（如外星人或飞船）都是一个surface。
    # display.set_mode() 返回的surface表示整个游戏窗口。我们激活游戏的动画循环后，每经过一次循环都将自动重绘这个surface

    # 创建一个名为screen的显示窗口，并指定窗口尺寸宽高：1200*800像素
    # screen = pygame.display.set_mode((1200, 800))
    """重构"""
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    """定义窗口名称"""
    pygame.display.set_caption("外星人入侵")

    """创建一艘飞船"""
    ship = Ship(ai_settings, screen)

    """创建一个用于存储子弹的编组"""
    bullets = Group()

    # 设置背景颜色(RGB:红0~255, 绿0~255, 蓝0~255；三原色的值0~255)
    # bg_color = (230, 230, 230)

    """开始游戏的主循环"""
    while True:
        # 监听键盘和鼠标事件；
        gf.check_events(ai_settings, screen, ship, bullets)
        # 根据移动标志调整飞船的位置
        ship.update()
        # 更新子弹的位置，并删除已消失的子弹
        gf.update_bullets(bullets)

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()