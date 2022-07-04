import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船所发射子弹的类。"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen   = ai_game.screen
        self.settings = ai_game.settings
        self.color    = self.settings.bullet_color

        #在（0,0）处创建一个表示子弹的矩形，再设置正确的位置。
        self.rect = pygame.Rect(0,0,self.settings.bullet_height,
                                self.settings.bullet_width)
        self.rect.midtop = ai_game.ship.rect.midtop

        #存储用小数表示子弹的位置
        self.x = float(self.rect.x)

    def update(self):
        """向右移动子弹"""
        #更新表示子弹位置。
        self.x+=self.settings.bullet_speed
        #更新表示子弹的rect的位置
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)