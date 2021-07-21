

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    # 引用参数self和screen
    # 里面的参数千万不要调乱顺序
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始化位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获得其外接矩形
        # pygame.image.load(内部是加载图片的路径)
        self.image = pygame.image.load('/Users/huanghui/python_work/Airplane-game/images/ship.bmp')

        # get_rect()是一个处理矩形的方法，也就是飞机贴图————这个处理方法就是获取这个贴图的坐标
        # self.rect.left为 获取贴图左侧坐标
        # self.rect.right 获取贴图右侧坐标
        self.rect = self.image.get_rect()
        # 把屏幕中心的矩形储存在screen_rect中，这个数值是根据玩家操控飞机时候不断获取的，通过 .screen来获取
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中间
        # .centerx把物体放在屏幕X轴方向的中央
        self.rect.centerx = self.screen_rect.centerx
        # .bottom底部的调用（把物体放在Y轴方向的屏幕底部）
        self.rect.bottom = self.screen_rect.bottom
        # 移动标志（将初始值设为False）
        # False一开始就是停止移动，True的话就是不停的移动
        self.moving_right = False
        self.moving_left = False
        # float()可以存储小数
        # float()只是储存数值，不储存其他东西
        # 所以最后需要把储存的数值返回给self.rect.centerx
        self.center = float(self.rect.centerx)


    def update(self):
        """根据移动标志调整飞船的位置"""

        """飞机贴图与箱体盒子是重叠的
           如果需要让飞机盒子模型不超出屏幕左右边缘，需要获取出屏幕左侧、右侧边缘的数值，
           屏幕左侧数值的获取，就是正数值，一般默认屏幕左下角为原点，往上（y轴方向）为y的正数值，往下为有的负数值，
           同理，原点往右（x轴方向）为x的正数值，往右为x的负数值，所以当x轴方向大于0时，飞机盒子在屏幕里面，正常运作，正常传递数值"""

        # self.rect_right 为矩形（飞机的箱体模型）右侧边缘的值
        # if self.moving_right:

        # self.screen_rect
        # 为玩家不断移动飞机盒子产生的数值

        # self.screen_rect.right
        # 为玩家不断移动飞机盒子，飞机盒子最右边所产生的数值

        # self.rect.right
        # 为返回飞机贴图的右边的 x 坐标

        # self.rect.right < self.screen_rect.right:
        # 意思是飞机贴图的右边的 x 坐标 小于 （玩家不断移动飞机盒子）飞机盒子最右边所产生的数值
        # 也就是说比对飞机贴图的的右侧边缘右边 与 箱体盒子的右边坐标
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 储存的数值为整数
            # 这里是把self.rect.centerx直接赋值
            # self.rect.centerx += 1
            # 这里是直接获取ship_seepd_factor的数值
            # self.center递增self.ai_settings.ship_speed_factor
            self.center += self.ai_settings.ship_speed_factor

        # self.rect.left 为矩形（飞机的箱体模型）左侧边缘的值
        # if self.moving_left:
        # 上面提到屏幕左下角为原点，x轴往右为正数值，所以检测飞机贴图左边坐标大于0就可以知道箱体盒子是否超出屏幕
        if self.moving_left and self.rect.left > 0:
            # 储存的数值为整数
            # self.rect.centerx -= 1
            # 这里是直接获取ship_seepd_factor的数值
            # self.center递减self.ai_settings.ship_speed_factor
            self.center -= self.ai_settings.ship_speed_factor



        # float()只是储存数值，不储存其他东西
        # 把 self.center += self.ai_settings.ship_speed_factor 的增加值储存在self.rect.centerx中
        # 把 self.center -= self.ai_settings.ship_speed_factor 的减少值储存在self.rect.centerx中
        # 所以最后需要把储存的数值返回给self.rect.centerx
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def run_game(self):
        alien = Alien(ai_settings, screen)

        while True:
            gf.check_events(ai_settings, screen, ship, bullets)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_screen(ai_settings, screen, ship, alien, bullets)

    def center_ship(self):
        self.center = self.screen_rect.centerx
