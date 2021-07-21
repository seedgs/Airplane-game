import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_settings, screen):

        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像
        self.image = pygame.image.load('/Users/huanghui/python_work/Airplane-game/images/alien.bmp')
        # 设置其rect属性
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 储存外星人的准确位置
        self.x = float(self.rect.x)
        # 外星人设置
        self.alien_speed_factor = 1

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        # +=为向右移动，-=为向左移动
        # 移动的数值为alien_speed_factor的设置
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        # 以屏幕左下角为基准，向右增大，向左减小
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
