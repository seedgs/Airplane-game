"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序
"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序
"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序


"""储存外星人入侵的所有设置"""

import file as f
class Settings():
    def __init__(self):
        # 屏幕尺寸
        self.screen_width = 1200
        self.screen_height = 800
        # 改变屏幕背景颜色
        self.bg_color = (230, 230, 230)
        # 控制飞船的移动速度
        self.ship_speed_factor = 9.5
        # 子弹设置
        # 设置子弹数
        self.bullet_speed_factor = 20
        # 设置子弹宽度
        self.bullet_width = 3
        # 设置子弹高度
        self.bullet_height = 15
        # 设置子弹颜色
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # self.alien_speed_factor表示外星人撞到屏幕边缘时，外星人群向下移动的速度
        self.alien_speed_factor = 1
        # 控制外星人群下落的速度
        self.fleet_drop_speed = 10
        self.ship_limit = 3
        # self.fleet_direction 的值为1表示向右移动，数值为-1表示向左移动
        # self.fleet_direction也可以设置为文本值，例如：left、right
        # 如果设置为left 或 right数值的话，就就必须编写 if-elif语句来检查外星人群的移动方向，所以 1 与 -1来判断左右是最为符合的
        # 外星人群向左移动，需要 减少 x坐标值
        # 外星人群向右移动，需要 增加 x坐标值
        self.fleet_direction = 1

        # 设置飞船
        self.ship_speed_factor = 1.5

        # self.radius = 20

        # 以什么样的速度加快游戏节奏
        # 用于控制游戏节奏，加快速度
        # 1表示游戏节奏始终不变
        self.speedup_scale = 1.1

        # 外星人点数的提高速度
        # 定义点数提高的速度为score_scale
        self.score_scale = 1.5

        # 表示玩家每提高一个等级，游戏的节奏就翻倍
        self.initialize_dynamic_settings()

        # # 统计信息文件路径
        # self.filename = 'file/stats.pkl'
        #
        # # 读取文件得最高分，在任何情况下都不应该重置最高得分
        # statsObj = f.load_file(self.filename)
        # if statsObj == 0:
        #     # 不存在文件则显示最高分0
        #     highScore = 0
        # else:
        #     for key, val in statsObj.items():
        #         # 获取文件最高分的值（当文件字段不止一个时候使用）
        #         if key == 'highScore':
        #             highScore = val
        # self.high_score = highScore


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 20
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右：为-1向左
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""

        # 为提高这些游戏元素的速度，我们将每个速度设置都乘以speedup_scale的值
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

