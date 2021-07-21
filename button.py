# 导入模块，让Pygame能够将文本渲染到屏幕上
# 也就是在屏幕上绘制按钮
import pygame.font
class Button():
    # msg是要在按钮中显示的文本
    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.screen = screen
        # self.screensize = screensize
        self.screen_rect = screen.get_rect()

        """设置按钮的尺寸和其他属性"""
        # 按钮尺寸
        self.width, self.height = 200, 50
        # 按钮颜色
        self.button_color = (0, 222, 0)
        # 文本颜色
        self.text_color = (255, 255, 255)
        # self.color = (100, 0, 110)
        # self.pos = 100, 100
        # self.radius = screen.get_height() / 2

        # self.centerx = int(screensize[0] * 0.5)
        # self.centery = int(screensize[0] * 0.5)
        # self.radius = 3

        # 我们指定使用什么字段来渲染文本，实参None让Pygame使用默认字体，48为文本字号
        self.font = pygame.font.SysFont(None, 48)
        # self.circular = pygame.draw.circle(screen, self.color, self.pos, self.radius, 25, 1)

        """创建按钮的rect对象，并使其居中"""
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # 为让按钮在屏幕居中，我们创建一个表示按钮的rect对象，并将其center属性设置为屏幕的center属性
        self.rect.center = self.screen_rect.center
        # self.circular.center = self.screen_rect.center



        """按钮的标签只需创建一次"""
        # Pygame将你要显示的字符串渲染为图像来处理文本，调用prep_msg()来处理这样的渲染
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        # True为开启屏幕抗锯齿的功能，如果不设置背景色，系统默认背景为透明色
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # 让文本图像在按钮上居中，根据文本创建一个rect
        self.msg_image_rect = self.msg_image.get_rect()
        # 并将其center属性设置为按钮的center属性
        self.msg_image_rect.center = self.rect.center

    # 绘制按钮的函数，绘制一个用颜色填充的按钮，再绘制文本
    def draw_button(self):
        # screen.fill()绘制表示按钮的矩形
        self.screen.fill(self.button_color, self.rect)
        # 向screen.blit()传递一副图像以及图像相关的rect对象
        self.screen.blit(self.msg_image, self.msg_image_rect)

        # self.screen.fill(self.color)