# 导入需要用到的库
import random
import pygame
# 设置背景屏幕前两个参数为坐标，后两个为屏幕长宽（也是背景图片的大小）这两个值根据选择的背景图片大小设定
SCREEN_RECT = pygame.Rect(0, 0, 462, 647)
# 设置每秒刷新
FRAME_PER_SEC = 60
# 调用pygame的创建静态事件方法
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建的第二个静态事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


# 创建游戏精灵类，传入pygame精灵类方法
class GameSprite(pygame.sprite.Sprite):
# 定义初始化方法
    def __init__(self, image_name, speedx=1, speedy=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speedx


# 创建背景类继承自游戏精灵类
class Background(GameSprite):
    def __init__(self, is_alt=False):
    # 传入背景图片（图片文件均存放在该目录直接使用图片名）背景滚动默认速度为1
        super().__init__('bj.png', speedy=1)
        if is_alt:

            self.rect.y = -self.rect.height

# 调用父类方法更新显示
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


# 创建敌机类
class Enemy(GameSprite):
    def __init__(self):
    # 调用父类方法传入敌机图片
        super().__init__('dj.png')
        self.rect.y = -self.rect.height
        self.speedx = random.randint(2, 7)
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            # 将精灵从精灵组中删除，精灵也会被删除
            self.kill()


class Hero(GameSprite):
    def __init__(self):
        super().__init__('hero.png', 0, 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 50
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        self.rect.y += self.speedy
        if self.rect.y <= 0:
             self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
             self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self):
        for i in range(2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__('zd.png', -3)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
