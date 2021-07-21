"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序
"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序
"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序





# # 导入模块
# import sys
# import pygame



# def run_game():
#     # 初始化背景设置，让pygame能够正常工作
#     pygame.init()
#     # 调用pygame.display.set_mode()来创建一个名为screen的显示窗口
#     # 实参(1200, 800)是一个元组，指定了游戏窗口的尺寸，通过这些尺寸值传递给pygame.display.set_mode()
#     # 我们创建了一个宽1200px，高800px的游戏窗口(可以自定义调整)
#     # screen是一个surface。在游戏中，每个元素都是一个surface
#     # pygame.display.set_mode((1200, 800))表示是这个游戏里面的游戏窗口，我们激活游戏的动画循环后，
#         # 每经过一次循环都将自动重绘这个surface(也就是重新加载一次游戏窗口)
#     screen = pygame.display.set_mode((1200, 800))
#
#     pygame.display.set_caption("Alien Invasion")
#
#     # 口号内为rga的颜色数值
#     bg_color = (252, 252, 252)
#     # 编译循环来监听事件
#     # 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见，在我们移动游戏元素时，pygame.display.file()将不断更新屏幕
#         # 以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果
#     while True:
#         # 访问pygame.event.get()监测到的时间 到 event中
#         for event in pygame.event.get():
#             # 当监听属性探测到用户点击关闭按钮的时候（pygame.OUIT就是指那个按钮），就退出游戏
#             if event.type == pygame.QUIT:
#                 # sys.exit()退出游戏
#                 sys.exit()
#             # 用背景色填充屏幕，每次循环都重绘屏幕，并加载颜色
#             screen.fill(bg_color)
#             # pygame.display.flip()让pygame绘制的屏幕可见
#             pygame.display.flip()
#
# # 调用类，并将初始化游戏并开始主循环
# run_game()


import pygame
# 从settings内加载Settings类
from settings import Settings
# 从ship内加载Ship类
from ship import Ship
# 把game_functions文件用gf替代，以后就可以用gf来引入

from alien import Alien



import game_functions as gf
# 从pygame.sprite加载Group
from pygame.sprite import Group
from game_stats import GameStats
from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    # screen = pygame.display.set_mode(这里面可以加入参数)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # pygame.display.set_caption()设置当前窗口标题
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    # 创建一个用于储存子弹的编组 Group()
    # while循环外面创建编组，就可以不用每次运行该循环都创建一个新的子弹编组
    bullets = Group()
    ship = Ship(ai_settings, screen)
    # 用来储存外星人的编组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    pygame.display.set_caption("Alien Invasion")
    """创建一个用于储存游戏统计信息的实例"""
    stats = GameStats(ai_settings)

    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play Keyboard Star")


    sb = Scoreboard(ai_settings, screen, stats)


    # 开始游戏主循环
    while True:
        # 监听各种逻辑方法
        # 也就是监听键盘按键，反馈给程序的数值，括号内就是各种监听数值
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 加载update方法
            ship.update()
            # screen.fill(ai_settings.bg_color)
            # 加载ship类里面的blitme函数

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)


        # bullets.update()
        # # 删除已消失的子弹
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        # # 此段检测子弹删除后是否为0
        # # print(len(bullets))

        # gf.update_aliens(ai_settings,  ship, aliens)
        # gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


        ship.blitme()

        pygame.display.flip()


run_game()




