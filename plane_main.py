# 导入刚创建的类的所有方法
from plane_sprites import*


class PlaneGame(object):

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

# 创建精灵
    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
# 游戏从这里开始
    def start_game(self):
        # 每隔一段时间触发一次事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 200)
        pygame.time.set_timer(HERO_FIRE_EVENT, 300)
        # 定义游戏循环
        while True:
         # 每秒运行该循环的次数
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

# 监听键盘按键
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        # 返回按键元祖
        keys_pressed = pygame.key.get_pressed()
        # 判断左和右是否同时按下
        if (keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_LEFT]) \
                or (keys_pressed[pygame.K_a] and keys_pressed[pygame.K_d]):
            self.hero.speedx = 0
        elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.hero.speedx = 3
        elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.hero.speedx = -3
        else:
            self.hero.speedx = 0
        if (keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]) \
                or (keys_pressed[pygame.K_w] and keys_pressed[pygame.K_s]):
            self.hero.speedy = 0
        elif keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            self.hero.speedy = -3
        elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            self.hero.speedy = 3
        else:
            self.hero.speedy = 0
      # 碰撞检测      
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        if pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True):
            self.__game_over()
# 精灵组刷新显示
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print('游戏结束')
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
