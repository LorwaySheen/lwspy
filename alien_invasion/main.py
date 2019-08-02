import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()       #初始化所有pygame模块
    ai_settings = Settings()        #创建settings对象
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))  ##初始化要显示的窗口或屏幕
    pygame.display.set_caption("Alien Invasion")        #设置当前窗口标题

    ship = Ship(ai_settings,screen)     #创建一艘飞船

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)


run_game()    
 