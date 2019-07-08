import pygame

"""负责管理飞船的大部分行为"""


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        """加载飞船图像并获取其外接矩形"""
        # load（）返回一个表示飞船的surface，并储存到self.image属性中
        self.image = pygame.image.load(r'images\ship.bmp')
        # get_rect() 获取相应surface的属性rect（矩形）
        # 将表示飞船的矩形存储在self.rect中
        self.rect = self.image.get_rect()
        # 将表示屏幕的矩形存储在 self.screen_rect 中
        self.screen_rect = screen.get_rect()

        """将每艘新飞船放在屏幕底部中央"""
        # 要将游戏元素居中，可设置相应 rect 对象的属性 center 、 centerx 或 centery
        # 要让游戏元素与屏幕边缘对齐，可使用属性 top 、 bottom 、 left 或 right
        # 要调整游戏元素的水平或垂直位置，可使用属性 x 和 y ，它们分别是相应矩形左上角的 x 和 y 坐标
        # 将飞船中心的x坐标设置为表示屏幕的矩形的属性 centerx
        self.rect.centerx = self.screen_rect.centerx
        # 将飞船下边缘的y坐标设置为表示屏幕的矩形的属性 bottom
        self.rect.bottom = self.screen_rect.bottom

        """初始化飞船左右移动标志"""
        self.moving_left = False
        self.moving_right = False

        # 在飞船的属性 center 中存储小数值
        self.center = float(self.rect.centerx)

    def blitme(self):
        """在制定位置绘制飞船"""
        # 根据 self.rect 指定的位置将图像绘制到屏幕上
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 当飞船左右移动标志为True时，飞船图片则向左或向右移动一个飞船速度
        # 控制飞船左侧最大移动边界：当飞船图片左侧像素大于0，则允许飞船继续向左边移动
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 控制飞船右侧最大移动边界：当飞船图片右侧像素小于窗口右侧最大像素值，则允许飞船继续向右边移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        # 每按一次方向键，更新飞船一次最新位置
        self.rect.centerx = self.center
