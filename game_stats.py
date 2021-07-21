import pickle
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        # 调用方法
        # 创建GameStats实例，玩家一开始也能调用
        self.reset_stats()
        # 游戏刚启动时处于活动状态
        # True为初始的时候处于活跃状态
        # False为初始的时候处于非活跃状态



        # 任何情况下都不应重置最高得分
        self.high_score = 0




        self.game_active = False

        # filename = 'highest_score.txt'
        #
        # with open(filename, 'r')as file_obj:
        #     self.high_score = str(file_obj)

        self.level = 1





    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""

        # 当前设置的统计信息：ships_left
        # ship_limit为一开始玩家拥有的飞船数，并储存在其中
        self.ships_left = self.ai_settings.ship_limit

        self.score = 0

        self.level = 1
        # self.load_high_score()


    # def save_high_score(self):
    #     f = open("/Users/huanghui/python_work/alien_invasion/highest_score.txt", 'wb')
    #     pickle.dump(str(self.high_score), f, 0)
    #     f.close()
    #
    # def load_high_score(self):
    #     f = open("/Users/huanghui/python_work/alien_invasion/highest_score.txt", 'rb')
    #     try:
    #         str_high_score = pickle.load(f)
    #
    #         self.high_score = int(str_high_score)
    #     except EOFError:
    #         self.high_score = 0
    #     finally:
    #         f.close()
