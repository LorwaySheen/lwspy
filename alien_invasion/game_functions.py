import sys
import pygame

def check_events(ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():        #从队列中获取事件，即侦听鼠标键盘事件
        if event.type == pygame.QUIT:       #检测到pygame.QUIT事件时调用sys.exit()退出游戏
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #向右移动飞船
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)       #每次循环重新绘制屏幕背景色
    ship.blitme()       
    pygame.display.flip()       #在屏幕上更新显示   