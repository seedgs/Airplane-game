"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序
"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序
"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序



import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形，再设置正确的位置
        # 创建矩形必须提供初始坐标，(0, 0)为左上角坐标
        # 当前飞机初始位置为水平居中，垂直屏幕底部，所以子弹的初始位置也是根据飞机的初始位置来设定的
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        # 因为子弹的发射初始位置是根据飞机动态射出的，子弹必须跟随飞机而射出，就是说飞机移动到哪里，子弹就必须从飞到哪里的飞机那里去发射

        # rect.centerx是飞船的水平坐标，我们也设置成子弹的水平坐标
        self.rect.centerx = ship.rect.centerx
        # 子弹是从飞船头部飞出去的，因为我们把飞船贴图与箱体模型重合了，所以从飞船顶部射出子弹，也就是从箱体模型射出子弹
        # 只要获取箱体顶部坐标给子弹即可
        self.rect.top = ship.rect.top

        # 存储用小数表示子弹位置
        # float() 是函数用于将整数和字符串转换成浮点数
        self.y = float(self.rect.y)
        # bullet_color子弹颜色
        self.color = ai_settings.bullet_color
        # bullet_speed_factor子弹速度
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        # 子弹从飞机盒子顶端发射出去，子弹在屏幕中向上移动，要从self.y中减去self.speed.factor的数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
