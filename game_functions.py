"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序
"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序
"""里面的参数千万不要调乱顺序"""
# 里面的参数千万不要调乱顺序



import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
# from alien import Alien

# def check_events(ship):
#     # 访问pygame.event.get()监测事件 到 event中
#     for event in pygame.event.get():
#         # 当监听属性探测到用户点击关闭按钮的时候（pygame.OUIT就是指那个按钮），就退出游戏
#         if event.type == pygame.QUIT:
#             sys.exit()
#         # KEYDOWN为当键盘  按下  的的时候（事件），也就是说pygame.event.get()监测事件 到 event中
#         # event的type属性监测到键盘按下的时候
#         elif event.type == pygame.KEYDOWN:
#             # （.key为按键，K_RIGHT键盘右方向键）
#             if event.key == pygame.K_RIGHT:
#                 #  也就是说当event的按键属性监测到用户按下键盘右方向键（K_RIGHT）时
#                 #  ship.rect.centerx的数值（也就是横向坐标）递增 1
#                 #  递增 1 的时候ship.moving_right为 True
#                 ship.rect.centerx += 1
#                 ship.moving_right = True
#             # 同理按下左键
#             elif event.key == pygame.K_LEFT:
#                 ship.rect.centerx -= 1
#                 ship.moving_left = True
#         # KEYUP为当键盘  抬起  的的时候（事件），也就是说pygame.event.get()监测事件 到 event中
#         # event的type属性监测到键盘按下的时候
#         elif event.type == pygame.KEYUP:
#             # （.key为按键，K_RIGHT键盘右方向键）
#             if event.key == pygame.K_RIGHT:
#                 #  也就是说当event的按键属性监测到用户按下键盘右方向键（K_RIGHT）时
#                 #  ship.moving_right为 False
#                 ship.moving_right = False
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = False

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 显示得分
    sb.show_score()

    # 在飞船和外星人后面重绘所有子弹

    # bullets.sprites()是返回bullets的列表，这个列表包含bullets的所有参数
    # 为在屏幕绘制出子弹，遍历bullets所有参数
    for bullet in bullets.sprites():
        # 并对每个参数都调用draw_bullets()
        bullet.draw_bullet()

    # 屏幕绘制出飞机
    ship.blitme()

    # 在屏幕上绘制编组中的每个外星人
    aliens.draw(screen)


    # 让最近绘制的屏幕可见
    pygame.display.flip()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 检测键盘  "下击"  时间的响应
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)


            # 当下击键盘s按键时，开始游戏
            if event.key == pygame.K_s:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        # .MOUSEBUTTONDOWN为调用pygame中的鼠标下击时间，以监测鼠标下击状态

        # 检测  "鼠标"  "下击"  时间的响应
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     # 监测鼠标x、y轴坐标，是为了无论在屏幕哪里点击，都会启动游戏的活跃状态
        #
        #     mouse_x, mouse_y = pygame.mouse.get_pos()
        #     check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        #

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """玩家单击Play按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    # if play_button.rect.collidepoint(mouse_x, mouse_y):

    # not stats.game_active为玩家点击Play按钮，游戏当前处于非活跃状态
    # 点击后处于活跃状态
    if button_clicked and not stats.game_active:
        """重置游戏统计信息"""
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()

        sb.prep_level()
        sb.prep_ships()





        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞机居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 隐藏鼠标
        # 当玩家点击屏幕上的Play按钮时，隐藏鼠标
        pygame.mouse.set_visible(False)


        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

    # elif not play_button.rect.collidepoint(mouse_x, mouse_y):
    #     stats.game_active = False




def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    # pygame.K_RIGHT:为监听键盘右键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # pygame.K_LEFT:为监听键盘左键
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # pygame.K_SPACE:为监听键盘空格键
    elif event.key == pygame.K_SPACE:


        # 通过按下空格按键去创建一颗新子弹

        new_bullet = Bullet(ai_settings, screen, ship)
        # 使用方法add加入编组bullets中
        # 将其加入到编组bullets中
        bullets.add(new_bullet)
        # 也可以写成这样去理解
        # bullets.add(Bullet(ai_settings, screen, ship))

    elif event.key == pygame.K_q:
        sys.exit()




        # # 创建新子弹并将其加入到编组bullets中
        # if len(bullets) < ai_settings.bullets_allowed:
        #     new_bullet = Bullet(ai_settings, screen, ship)
        #     bullets.add(new_bullet)



def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)





def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


# def update_bullets(ai_settings, screen, ship, aliens, bullets):
#     """更新子弹的位置，并删除已消失的子弹"""
#     # 更新子弹位置
#     bullets.update()
#
#     for bullet in bullets.copy():
#         if bullet.rect.bottom <= 0:
#             bullets.remove(bullet)
#     # 此段检测子弹删除后是否为0
#     # print(len(bullets))
#
#     """子弹射击，外星人消失"""
#     # 检查是否有子弹击中了外星人
#     # 如果是这样，就删除相应的子弹和外星人
#     # 新增的这行代卖遍历组bullets中的每颗子弹，再遍历组aliens中的每个外星人。
#     # 每当有子弹和外星人的rect重叠时,groupcollide()就在它返回的字典中添加一个键-值对。
#     # 实参False 和 True告诉Pygame删除发生碰撞的子弹和外星人
#     collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
#
#
#     # 外星人被子弹射光后，重新刷新外星人
#     # 检测编组aliens(外星人)是否为空
#     if len(aliens) == 0:
#         # 删除现有的子弹并新建一群外星人
#         # bullets.empty()中的empty()为快速创建数组，里面的数组均为空
#         # 如果aliens为空，就调用方法empty()删除编组中余下的所有外星人，从而删除所有的子弹，再次在屏幕上显示一群外星人
#         bullets.empty()
#         create_fleet(ai_settings, screen, ship, aliens)


# 重构代码
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

# 此函数为检测子弹和外星人之间的碰撞
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        # 有子弹撞到外星人时，pygame返回一个字典（collisions），检查这个字典是否存在，就将得分加上一个外星人值的点数

        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 删除现有的子弹，加快游戏节奏，并穿件一群新的外星人
        bullets.empty()
        ai_settings.increase_speed()


        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)





def get_number_aliens_x(ai_settings, alien_width):
    """计算水平宽度可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_y(ai_settings, alien_height):
    """计算垂直高度可容纳多少个外星人"""
    available_space_y = ai_settings.screen_height - ship_height - alien_height
    number_aliens_y = available_space_y / (2 * alien_height - ship_height)
    return number_aliens_y


# 这个函数的意义就是把绘制外星人循环的方法放在这个函数里面
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前"""

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # alien_height = alien.rect.height
    # alien.y = alien_height + 2 * alien_height * alien_number_y + ship_height
    # alien.rect.y = alien.y

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算每行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    # get_number_aliens_x 是水平方向计算的函数
    # get_number_rows 是垂直方向计算的函数
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # for alien_number in range(number_aliens_x):
    #     create_alien(ai_settings, screen, aliens, alien_number, row_number)

    # 以下两个方法都可以
    # 这里创建循环，然后调用函数的循环方法的参数
    for alien_number in range(number_aliens_x):
        for row_number in range(number_rows):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

    # for row_number in range(number_rows):
    #     for alien_number in range(number_aliens_x):
    #         create_alien(ai_settings, screen, aliens, alien_number, row_number)



def get_number_rows(ai_settings, ship_height, alien_height):
    # ai_settings.screen_height为屏幕高度
    # ship_height为飞机本体的高度
    # alien_height为外星人的本体高度
    # available_space_y = ai_settings.screen_height - 5 * alien_height
    # 将屏幕高度减去第一行外星人的上边距(外星人高度)、飞船的高度以及最初外星人群与飞船的距离(外星人高度的两倍)
    # available_space_y = ai_settings.screen_height - alien_height - ship_height

    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    # 要求出外星人的行数，必须算出外星人可用空间（也就是上面的available_space_y）
    # 可用空间除以外星人的高度（但是要注意，这个外星人的高度必须是两倍外星人的高度，因为有间距，也就是两倍外星人的高度的间距）
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """更新外星人群中所有外星人的位置"""
    # 检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    # spritecollideany()就是为stats的传参的   碰撞的方法
    # 此方法接受两个实参，ship是飞船(玩家控制)，aliens是外星人群(电脑控制)


    #     ******************检查飞船是否与外星人群有碰撞******************
    if pygame.sprite.spritecollideany(ship, aliens):
        # print("Ship hit!!!")
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    """检查是否有外星人到达屏幕底端"""
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    # 遍历外星人"群" aliens.sprites()的方法在alien.py页面内
    # aliens.sprites()返回True，外星人就位于屏幕边缘，需要改变外星人群的方向
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    # 同样遍历外星人
    for alien in aliens.sprites():
        # 使其下移fleet_drop_speed设置的值
        # 如果为"+"号，外星人群会向下移动
        # 如果为"—"号，外星人群会向上移动忍
        # 如果吧alien.rect.y的y，改成行，显示结果就是外星人群会不断左右移
        alien.rect.y += ai_settings.fleet_drop_speed
    # 将ai_settings.fleet_drop_speed的值修改为-1的乘积
    ai_settings.fleet_direction *= -1



class GameStars():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settiings
        self,rect_stats()

    def rest_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit



# 此函数是在飞船与外星人群碰撞时，需要做出的反应
# 1、飞船碰到外星人生命值（飞机个数）-1
# 2、飞船碰到外星人要暂停（让玩家知道被撞到了）
# 3、飞船碰到外星人后，飞船重新出现在屏幕底端的中央位置
# 4、飞船碰到外星人后，外星人群重新返回屏幕顶端中央
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应被外形热撞到的飞船"""

    # empty()函数为清空的作用
    # aliens.empty()清空外星人
    # bullets.empty()清空子弹
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人，并将飞船放到屏幕底端中央
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


    # 当外星人碰到飞船的时候：
    #     如果此时飞船数量大于0时（也就是生命值没有归零时），外星人碰到飞船时，飞船数量-1，且游戏暂停1时间单位
    #  否则
    #     飞船数量为零（生命值归零状态）。外星人碰到飞船时，游戏此时要处于不活跃状态（也就是结束）

    # 这里的stats为储存游戏统计信息，根据这个信息来判断外星人是否于飞船发生碰撞，从而展开功能的写入
    if stats.ships_left > 0:
        # 当外星人群撞到飞机的时候，飞机数量-1
       stats.ships_left -= 1
        # 更新记分牌
       sb.prep_ships()
        # 同时暂停一下，让玩家反应过来
       sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)




def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        # 为什么 alien.rect.bottom 要大于等于 screen_rect.bottom ？？？？？
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()











# def create_fleet(ai_settings, screen, aliens):
#     """创建外星人群"""
#
#     # 飞机垂直方向的排布计算
#
#     # 创建飞机的高度
#     ship_height = alien.rect.height
#     # 创建外星人的高度
#     alien_height = alien.rect.height
#     # 需要布局的外星人的区域的高度 = 屏幕高度 - 飞机高度（只有一个） - 一个外星人的高度
#     available_space_y = ai_settings.screen_height - ship_height - alien_height
#     # 需要布局的外星人的区域的高度的个数 = 需要布局的外星人的区域的高度 / （外星人的高度 + 外星人的高度 - 飞机的高度）
#     number_aliens_y = available_space_y / (2 * alien_height - ship_height)
#     # 创建需要的作用就是添加循环，把外星人布局上屏幕
#     for alien_number_y in range(number_aliens_y):
#         # 创建第一个外星人，通过y坐标加入当前行
#         alien = Alien(ai_settings, screen)
#         # 外星人一坐标上 = 外星人的高度 + 2 * 外星人的高度 *  需要布局的外星人的区域的高度的个数 + 飞机高度
#         # 公式里的：外星人高度、 飞机高度是出血位置（就是流出的空位）
#         #         2 * 外星人的高度 是 一个外星人的高度与一个外星人高度的空白位置
#         alien.y = alien_height + 2 * alien_height * alien_number_y + ship_height
#         alien.rect.y = alien.y
#         # 将每个外星人都添加进编组
#         alien.add(alien)
#
#
#     # 飞机水平方向的排布计算
#
#     # 创建一个外星人，并计算一行可容纳多少个外星人
#     # 外星人间距为外星人宽度
#     #  alien = Alien(ai_settings, screen)为创建一个外星人
#     alien = Alien(ai_settings, screen)
#     #  从外星人的rect属性中获取外星人的宽度
#     alien_width = alien.rect.width
#     # alien_height = alien.rect.height
#     # ship_height = ship.rect.height
#     # ai_settings.screen_width为屏幕宽度
#     # alien_width为外星人宽度
#     # 此公式意思是：外星人不能贴在左右屏幕上，要有出血位，所以屏幕左右两边各减去一个外星人的宽度
#     available_space_x = ai_settings.screen_width - 2 * alien_width
#     # 整个公式表示，外星人的充满整个屏幕（减去左右一个外星人的位置）的个数为（同时满足间距为一个外星人的宽度）：屏幕宽度除去两个外星人的宽度 = 外星人水平放置的个数
#     number_aliens_x = int(available_space_x / (2 * alien_width))
#     for alien_number_x in range(number_aliens_x):
#         # 创建第一个外星人，通过X坐标加入当前行
#         alien = Alien(ai_settings, screen)
#         # alien_width为外星人宽度
#         # alien_number为外星人的个数
#         # alien_width * alien_number为所有外星人的总宽度
#         # 2 * alien_width * alien_number两倍外星人的总宽度（包括间距）
#         # alien_width + 2 * alien_width * alien_number_x为空出最右边一个外星人的宽度
#         alien.x = alien_width + 2 * alien_width * alien_number
#         alien.rect.x = alien.x
#         # 将每个外星人都添加进编组
#         aliens.add(alien)


