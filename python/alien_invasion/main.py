import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

'''
def run_game():
    pygame.init()      #初始化所有pygame模块
    screen = pygame.display.set_mode((1200,800))       #初始化要显示的窗口或屏幕
    pygame.display.set_caption("Alien Invasion")       #设置当前窗口标题
    bg_color = (230,230,230)       #设置背景色
'''

    while True:
        for event in pygame.event.get():        #从队列中获取事件，即侦听鼠标键盘事件
            if event.type == pygame.QUIT:       #检测到pygame.QUIT事件时调用sys.exit()退出游戏
                sys.exit()
        
#       screen.fill(bg_color)       #每次循环重新绘制屏幕背景色
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()       #在屏幕上更新显示

run_game()    
