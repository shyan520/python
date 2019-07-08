import sys
import pygame

from group_two.bullet import Bullet

"""游戏主题功能"""


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    # 判断按下的键为向左方向键，飞船向左移动标志值设置成True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 判断按下的键为向右方向键，飞船向右移动标志值设置成True
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # 创建一颗子弹，并将其加入到编组 bullets 中
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """响应松开"""
    # 判断松开的键为向左方向键，飞船向左移动标志值设置成False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    # 判断松开的键为向右方向键，飞船向右移动标志值设置成False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    # 监听键盘和鼠标事件；所有键盘和鼠标事件都将促使for循环运行
    for event in pygame.event.get():
        # 如果玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT事件
        if event.type == pygame.QUIT:
            # 退出游戏
            sys.exit()
        # 判断是否检测到键盘按键KEYDOWN 事件，当检测到后
        elif event.type == pygame.KEYDOWN:
            # 响应按键
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # 判断是否检测到键盘按键KEYUP 事件，当检测到后
        elif event.type == pygame.KEYUP:
            # 响应松开
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    # 用背景色填充屏幕；这个方法只接受一个实参：一种颜色
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    """将飞船绘制到屏幕上，确保它出现在背景前面"""
    ship.blitme()

    # 命令Pygame让最近绘制的屏幕可见；它在每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见
    # 在我们移动游戏元素时，pygame.display.flip()将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    """删除已消失的子弹"""
    # 在 for 循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本。使用了方法 copy() 来设置 for 循环，这让我们能够在循环中修改 bullets
    for bullet in bullets.copy():
        # 检查每颗子弹，看看它是否已从屏幕顶端消失
        if bullet.rect.bottom <= 0:
            # 如果是这样，就将其从 bullets 中删除
            bullets.remove(bullet)
    # 我们使用了一条 print 语句，以显示当前还有多少颗子弹，从而核实已消失的子弹确实删除了
    # print(len(bullets))


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建新子弹并将其加入到编组 bullets 中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)