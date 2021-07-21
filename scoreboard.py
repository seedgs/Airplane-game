import pygame.font

from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """显示得分信息的类"""
    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分设计的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats


        # 显示得分信息时使用的字体设置
        # 设置文本颜色
        self.text_color = (30, 30, 30)
        # 实例化字体对象
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        # 将文本转换为图像
        self.prep_score()
        # 准备包含最高得分和当前得分的图像
        self.prep_high_score()

        self.prep_level()
        self.prep_ships()
        # self.prep_new_high_score()


    def prep_high_score(self):
        """最高得分转换为渲染的图像"""

        # high_score_str = str(self.stats.high_score)

        # 把最高得分圆整到最近的10的整数倍
        high_score = int(round(self.stats.high_score, -1))
        # 添加了用逗号表示的千分位分隔符
        high_score_str = "{:,}".format(high_score)
        # 根据最高得分生成一副图像
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)


        self.high_score_rect = self.high_score_image.get_rect()
        # 使其水平居中(伪)
        self.high_score_rect.left = self.score_rect.left - 600
        # 将其top属性设置为当前得分图像的top属性
        self.high_score_rect.top = 20

        #写入上一次得分
        filename = 'highest_score.txt'

        with open(filename, 'w')as file_obj:
            file_obj.write(high_score_str)





    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10



    def prep_ships(self):
        """显示还余下多少艘飞船"""
        # 创建一个空编组，用于储存飞船实例
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)



    def prep_score(self):
        # 将得分转换为一幅渲染的图像
        # 把数字转化成字符串
        score_str = str(self.stats.score)

        rounded_score = int(round(self.stats.score, -1))
        # 这里的"{:,}"是为了在得分的时候，得分的分数超过1000的时候，会变成1,000，而不是1000
        score_str = "{:,}".format(rounded_score)

        # 再把字符串传递给创建图像的.render
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # self.screen.blit(self.new_high_score_image, self.new_shigh_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


