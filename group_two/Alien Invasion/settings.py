"""创建游戏参数设置类"""


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置；宽高单位：像素
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        """设置飞船速度"""
        self.ship_speed_factor = 1.5

        """子弹设置"""
        # 初始化子弹速度
        self.bullet_speed_factor = 1
        # 初始化子弹宽度
        self.bullet_width = 3
        # 初始化子弹高度
        self.bullet_height = 10
        # 初始化子弹的填充颜色
        self.bullet_color = 60, 60, 60
        # 将未消失的子弹数限制为3颗
        self.bullets_allowed = 3
