import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    "管理游戏资源和行为的类"

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings =Settings()

        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height= self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship= Ship(self)
        self.bullets = pygame.sprite.Group()

        #设置背景色
        self.bg_color = (230,230,230)

        self.screen = pygame.display.set_mode((1200,800))

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()


    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """响应按键"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """响应松开"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        #更新子弹的位置
        self.bullets.update()

        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
    #创建游戏实例并进行游戏
    ai = AlienInvasion()
    ai.run_game()